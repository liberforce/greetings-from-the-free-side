#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from urllib.error import URLError
from urllib.parse import quote, urlparse, urlsplit, urlunsplit
from urllib.request import urlretrieve

# because logging.setLoggerClass has to be called before logging.getLogger
from pelican.log import init
from pelican.settings import read_settings
from pelican.utils import SafeDatetime, slugify

from gandiblog2pelican.parsers.dotclear import dc2fields
from gandiblog2pelican.parsers.wordpress import wp2fields
from gandiblog2pelican.parsers.common import get_filename, xml_to_soup

logger = logging.getLogger(__name__)


def decode_wp_content(content, br=True):
    pre_tags = {}
    if content.strip() == "":
        return ""

    content += "\n"
    if "<pre" in content:
        pre_parts = content.split("</pre>")
        last_pre = pre_parts.pop()
        content = ""
        pre_index = 0

        for pre_part in pre_parts:
            start = pre_part.find("<pre")
            if start == -1:
                content = content + pre_part
                continue
            name = "<pre wp-pre-tag-{0}></pre>".format(pre_index)
            pre_tags[name] = pre_part[start:] + "</pre>"
            content = content + pre_part[0:start] + name
            pre_index += 1
        content = content + last_pre

    content = re.sub(r"<br />\s*<br />", "\n\n", content)
    allblocks = (
        "(?:table|thead|tfoot|caption|col|colgroup|tbody|tr|"
        "td|th|div|dl|dd|dt|ul|ol|li|pre|select|option|form|"
        "map|area|blockquote|address|math|style|p|h[1-6]|hr|"
        "fieldset|noscript|samp|legend|section|article|aside|"
        "hgroup|header|footer|nav|figure|figcaption|details|"
        "menu|summary)"
    )
    content = re.sub(r"(<" + allblocks + r"[^>]*>)", "\n\\1", content)
    content = re.sub(r"(</" + allblocks + r">)", "\\1\n\n", content)
    #    content = content.replace("\r\n", "\n")
    if "<object" in content:
        # no <p> inside object/embed
        content = re.sub(r"\s*<param([^>]*)>\s*", "<param\\1>", content)
        content = re.sub(r"\s*</embed>\s*", "</embed>", content)
        #    content = re.sub(r'/\n\n+/', '\n\n', content)
    pgraphs = filter(lambda s: s != "", re.split(r"\n\s*\n", content))
    content = ""
    for p in pgraphs:
        content = content + "<p>" + p.strip() + "</p>\n"
    # under certain strange conditions it could create
    # a P of entirely whitespace
    content = re.sub(r"<p>\s*</p>", "", content)
    content = re.sub(r"<p>([^<]+)</(div|address|form)>", "<p>\\1</p></\\2>", content)
    # don't wrap tags
    content = re.sub(r"<p>\s*(</?" + allblocks + r"[^>]*>)\s*</p>", "\\1", content)
    # problem with nested lists
    content = re.sub(r"<p>(<li.*)</p>", "\\1", content)
    content = re.sub(r"<p><blockquote([^>]*)>", "<blockquote\\1><p>", content)
    content = content.replace("</blockquote></p>", "</p></blockquote>")
    content = re.sub(r"<p>\s*(</?" + allblocks + "[^>]*>)", "\\1", content)
    content = re.sub(r"(</?" + allblocks + r"[^>]*>)\s*</p>", "\\1", content)
    if br:

        def _preserve_newline(match):
            return match.group(0).replace("\n", "<WPPreserveNewline />")

        content = re.sub(r"/<(script|style).*?<\/\\1>/s", _preserve_newline, content)
        # optionally make line breaks
        content = re.sub(r"(?<!<br />)\s*\n", "<br />\n", content)
        content = content.replace("<WPPreserveNewline />", "\n")
    content = re.sub(r"(</?" + allblocks + r"[^>]*>)\s*<br />", "\\1", content)
    content = re.sub(
        r"<br />(\s*</?(?:p|li|div|dl|dd|dt|th|pre|td|ul|ol)[^>]*>)", "\\1", content
    )
    content = re.sub(r"\n</p>", "</p>", content)

    if pre_tags:

        def _multi_replace(dic, string):
            pattern = r"|".join(map(re.escape, dic.keys()))
            return re.sub(pattern, lambda m: dic[m.group()], string)

        content = _multi_replace(pre_tags, content)

    return content


def blogger2fields(xml):
    """Opens a blogger XML file, and yield Pelican fields"""

    soup = xml_to_soup(xml)
    entries = soup.feed.findAll("entry")
    for entry in entries:
        raw_kind = entry.find(
            "category", {"scheme": "http://schemas.google.com/g/2005#kind"}
        ).get("term")
        if raw_kind == "http://schemas.google.com/blogger/2008/kind#post":
            kind = "article"
        elif raw_kind == "http://schemas.google.com/blogger/2008/kind#comment":
            kind = "comment"
        elif raw_kind == "http://schemas.google.com/blogger/2008/kind#page":
            kind = "page"
        else:
            continue

        try:
            assert kind != "comment"
            filename = entry.find("link", {"rel": "alternate"})["href"]
            filename = os.path.splitext(os.path.basename(filename))[0]
        except (AssertionError, TypeError, KeyError):
            filename = entry.find("id").string.split(".")[-1]

        title = entry.find("title").string or ""

        content = entry.find("content").string
        raw_date = entry.find("published").string
        if hasattr(SafeDatetime, "fromisoformat"):
            date_object = SafeDatetime.fromisoformat(raw_date)
        else:
            date_object = SafeDatetime.strptime(raw_date[:23], "%Y-%m-%dT%H:%M:%S.%f")
        date = date_object.strftime("%Y-%m-%d %H:%M")
        author = entry.find("author").find("name").string

        # blogger posts only have tags, no category
        tags = [
            tag.get("term")
            for tag in entry.findAll(
                "category", {"scheme": "http://www.blogger.com/atom/ns#"}
            )
        ]

        # Drafts have <app:control><app:draft>yes</app:draft></app:control>
        status = "published"
        try:
            if entry.find("control").find("draft").string == "yes":
                status = "draft"
        except AttributeError:
            pass

        yield (title, content, filename, date, author, None, tags, status, kind, "html")


def posterous2fields(api_token, email, password):
    """Imports posterous posts"""
    import base64
    from datetime import timedelta
    import json
    import urllib.request as urllib_request

    def get_posterous_posts(api_token, email, password, page=1):
        base64string = base64.encodestring(
            ("%s:%s" % (email, password)).encode("utf-8")
        ).replace("\n", "")
        url = (
            "http://posterous.com/api/v2/users/me/sites/primary/"
            "posts?api_token=%s&page=%d"
        ) % (api_token, page)
        request = urllib_request.Request(url)
        request.add_header("Authorization", "Basic %s" % base64string.decode())
        handle = urllib_request.urlopen(request)
        posts = json.loads(handle.read().decode("utf-8"))
        return posts

    page = 1
    posts = get_posterous_posts(api_token, email, password, page)
    settings = read_settings()
    subs = settings["SLUG_REGEX_SUBSTITUTIONS"]
    while len(posts) > 0:
        posts = get_posterous_posts(api_token, email, password, page)
        page += 1

        for post in posts:
            slug = post.get("slug")
            if not slug:
                slug = slugify(post.get("title"), regex_subs=subs)
            tags = [tag.get("name") for tag in post.get("tags")]
            raw_date = post.get("display_date")
            date_object = SafeDatetime.strptime(raw_date[:-6], "%Y/%m/%d %H:%M:%S")
            offset = int(raw_date[-5:])
            delta = timedelta(hours=(offset / 100))
            date_object -= delta
            date = date_object.strftime("%Y-%m-%d %H:%M")
            kind = "article"  # TODO: Recognise pages
            status = "published"  # TODO: Find a way for draft posts

            yield (
                post.get("title"),
                post.get("body_cleaned"),
                slug,
                date,
                post.get("user").get("display_name"),
                [],
                tags,
                status,
                kind,
                "html",
            )


def tumblr2fields(api_key, blogname):
    """ Imports Tumblr posts (API v2)"""
    import json
    import urllib.request as urllib_request

    def get_tumblr_posts(api_key, blogname, offset=0):
        url = (
            "http://api.tumblr.com/v2/blog/%s.tumblr.com/"
            "posts?api_key=%s&offset=%d&filter=raw"
        ) % (blogname, api_key, offset)
        request = urllib_request.Request(url)
        handle = urllib_request.urlopen(request)
        posts = json.loads(handle.read().decode("utf-8"))
        return posts.get("response").get("posts")

    offset = 0
    posts = get_tumblr_posts(api_key, blogname, offset)
    settings = read_settings()
    subs = settings["SLUG_REGEX_SUBSTITUTIONS"]
    while len(posts) > 0:
        for post in posts:
            title = (
                post.get("title")
                or post.get("source_title")
                or post.get("type").capitalize()
            )
            slug = post.get("slug") or slugify(title, regex_subs=subs)
            tags = post.get("tags")
            timestamp = post.get("timestamp")
            date = SafeDatetime.fromtimestamp(int(timestamp)).strftime(
                "%Y-%m-%d %H:%M:%S"
            )
            slug = (
                SafeDatetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d-") + slug
            )
            format = post.get("format")
            content = post.get("body")
            type = post.get("type")
            if type == "photo":
                if format == "markdown":
                    fmtstr = "![%s](%s)"
                else:
                    fmtstr = '<img alt="%s" src="%s" />'
                content = ""
                for photo in post.get("photos"):
                    content += "\n".join(
                        fmtstr
                        % (photo.get("caption"), photo.get("original_size").get("url"))
                    )
                content += "\n\n" + post.get("caption")
            elif type == "quote":
                if format == "markdown":
                    fmtstr = "\n\n&mdash; %s"
                else:
                    fmtstr = "<p>&mdash; %s</p>"
                content = post.get("text") + fmtstr % post.get("source")
            elif type == "link":
                if format == "markdown":
                    fmtstr = "[via](%s)\n\n"
                else:
                    fmtstr = '<p><a href="%s">via</a></p>\n'
                content = fmtstr % post.get("url") + post.get("description")
            elif type == "audio":
                if format == "markdown":
                    fmtstr = "[via](%s)\n\n"
                else:
                    fmtstr = '<p><a href="%s">via</a></p>\n'
                content = (
                    fmtstr % post.get("source_url")
                    + post.get("caption")
                    + post.get("player")
                )
            elif type == "video":
                if format == "markdown":
                    fmtstr = "[via](%s)\n\n"
                else:
                    fmtstr = '<p><a href="%s">via</a></p>\n'
                source = fmtstr % post.get("source_url")
                caption = post.get("caption")
                players = "\n".join(
                    player.get("embed_code") for player in post.get("player")
                )
                content = source + caption + players
            elif type == "answer":
                title = post.get("question")
                content = (
                    "<p>"
                    '<a href="%s" rel="external nofollow">%s</a>'
                    ": %s"
                    "</p>\n"
                    " %s"
                    % (
                        post.get("asking_name"),
                        post.get("asking_url"),
                        post.get("question"),
                        post.get("answer"),
                    )
                )

            content = content.rstrip() + "\n"
            kind = "article"
            status = "published"  # TODO: Find a way for draft posts

            yield (
                title,
                content,
                slug,
                date,
                post.get("blog_name"),
                [type],
                tags,
                status,
                kind,
                format,
            )

        offset += len(posts)
        posts = get_tumblr_posts(api_key, blogname, offset)


def feed2fields(file):
    """Read a feed and yield pelican fields"""
    import feedparser

    d = feedparser.parse(file)
    settings = read_settings()
    subs = settings["SLUG_REGEX_SUBSTITUTIONS"]
    for entry in d.entries:
        date = (
            time.strftime("%Y-%m-%d %H:%M", entry.updated_parsed)
            if hasattr(entry, "updated_parsed")
            else None
        )
        author = entry.author if hasattr(entry, "author") else None
        tags = [e["term"] for e in entry.tags] if hasattr(entry, "tags") else None

        slug = slugify(entry.title, regex_subs=subs)
        kind = "article"
        yield (
            entry.title,
            entry.description,
            slug,
            date,
            author,
            [],
            tags,
            None,
            kind,
            "html",
        )


def build_header(
    title, date, author, categories, tags, slug, status=None, attachments=None
):
    """Build a header from a list of fields"""

    from docutils.utils import column_width

    header = "%s\n%s\n" % (title, "#" * column_width(title))
    if date:
        header += ":date: %s\n" % date
    if author:
        header += ":author: %s\n" % author
    if categories:
        header += ":category: %s\n" % ", ".join(categories)
    if tags:
        header += ":tags: %s\n" % ", ".join(tags)
    if slug:
        header += ":slug: %s\n" % slug
    if status:
        header += ":status: %s\n" % status
    if attachments:
        header += ":attachments: %s\n" % ", ".join(attachments)
    header += "\n"
    return header


def build_markdown_header(
    title, date, author, categories, tags, slug, status=None, attachments=None
):
    """Build a header from a list of fields"""
    header = "Title: %s\n" % title
    if date:
        header += "Date: %s\n" % date
    if author:
        header += "Author: %s\n" % author
    if categories:
        header += "Category: %s\n" % ", ".join(categories)
    if tags:
        header += "Tags: %s\n" % ", ".join(tags)
    if slug:
        header += "Slug: %s\n" % slug
    if status:
        header += "Status: %s\n" % status
    if attachments:
        header += "Attachments: %s\n" % ", ".join(attachments)
    header += "\n"
    return header


def get_ext(out_markup, in_markup="html"):
    if in_markup == "markdown" or out_markup == "markdown":
        ext = ".md"
    else:
        ext = ".rst"
    return ext


def get_out_filename(
    output_path,
    filename,
    ext,
    kind,
    dirpage,
    dircat,
    categories,
    wp_custpost,
    slug_subs,
):
    filename = os.path.basename(filename)

    # Enforce filename restrictions for various filesystems at once; see
    # http://en.wikipedia.org/wiki/Filename#Reserved_characters_and_words
    # we do not need to filter words because an extension will be appended
    filename = re.sub(r'[<>:"/\\|?*^% ]', "-", filename)  # invalid chars
    filename = filename.lstrip(".")  # should not start with a dot
    if not filename:
        filename = "_"
    filename = filename[:249]  # allow for 5 extra characters

    out_filename = os.path.join(output_path, filename + ext)
    # option to put page posts in pages/ subdirectory
    if dirpage and kind == "page":
        pages_dir = os.path.join(output_path, "pages")
        if not os.path.isdir(pages_dir):
            os.mkdir(pages_dir)
        out_filename = os.path.join(pages_dir, filename + ext)
    elif not dirpage and kind == "page":
        pass
    # option to put wp custom post types in directories with post type
    # names. Custom post types can also have categories so option to
    # create subdirectories with category names
    elif kind != "article":
        if wp_custpost:
            typename = slugify(kind, regex_subs=slug_subs)
        else:
            typename = ""
            kind = "article"
        if dircat and (len(categories) > 0):
            catname = slugify(categories[0], regex_subs=slug_subs)
        else:
            catname = ""
        out_filename = os.path.join(output_path, typename, catname, filename + ext)
        if not os.path.isdir(os.path.join(output_path, typename, catname)):
            os.makedirs(os.path.join(output_path, typename, catname))
    # option to put files in directories with categories names
    elif dircat and (len(categories) > 0):
        catname = slugify(categories[0], regex_subs=slug_subs)
        out_filename = os.path.join(output_path, catname, filename + ext)
        if not os.path.isdir(os.path.join(output_path, catname)):
            os.mkdir(os.path.join(output_path, catname))

    return out_filename


def get_attachments(xml):
    """returns a dictionary of posts that have attachments with a list
    of the attachment_urls
    """
    soup = xml_to_soup(xml)
    items = soup.rss.channel.findAll("item")
    names = {}
    attachments = []

    for item in items:
        kind = item.find("post_type").string
        post_name = item.find("post_name").string
        post_id = item.find("post_id").string

        if kind == "attachment":
            attachments.append(
                (item.find("post_parent").string, item.find("attachment_url").string)
            )
        else:
            filename = get_filename(post_name, post_id)
            names[post_id] = filename
    attachedposts = defaultdict(set)
    for parent, url in attachments:
        try:
            parent_name = names[parent]
        except KeyError:
            # attachment's parent is not a valid post
            parent_name = None

        attachedposts[parent_name].add(url)
    return attachedposts


def download_attachments(output_path, urls):
    """Downloads WordPress attachments and returns a list of paths to
    attachments that can be associated with a post (relative path to output
    directory). Files that fail to download, will not be added to posts"""
    locations = {}
    for url in urls:
        path = urlparse(url).path
        # teardown path and rebuild to negate any errors with
        # os.path.join and leading /'s
        path = path.split("/")
        filename = path.pop(-1)
        localpath = ""
        for item in path:
            if sys.platform != "win32" or ":" not in item:
                localpath = os.path.join(localpath, item)
        full_path = os.path.join(output_path, localpath)

        # Generate percent-encoded URL
        scheme, netloc, path, query, fragment = urlsplit(url)
        path = quote(path)
        url = urlunsplit((scheme, netloc, path, query, fragment))

        if not os.path.exists(full_path):
            os.makedirs(full_path)
        print("downloading {}".format(filename))
        try:
            urlretrieve(url, os.path.join(full_path, filename))
            locations[url] = os.path.join(localpath, filename)
        except (URLError, IOError) as e:
            # Python 2.7 throws an IOError rather Than URLError
            logger.warning("No file could be downloaded from %s\n%s", url, e)
    return locations


def is_pandoc_needed(in_markup):
    return in_markup in ("html", "wp-html")


def get_pandoc_version():
    cmd = ["pandoc", "--version"]
    try:
        output = subprocess.check_output(cmd, universal_newlines=True)
    except (subprocess.CalledProcessError, OSError) as e:
        logger.warning("Pandoc version unknown: %s", e)
        return ()

    return tuple(int(i) for i in output.split()[1].split("."))


def update_links_to_attached_files(content, attachments):
    for old_url, new_path in attachments.items():
        # url may occur both with http:// and https://
        http_url = old_url.replace("https://", "http://")
        https_url = old_url.replace("http://", "https://")
        for url in [http_url, https_url]:
            content = content.replace(url, "{static}" + new_path)
    return content


def fields2pelican(
    fields,
    out_markup,
    output_path,
    dircat=False,
    strip_raw=False,
    disable_slugs=False,
    dirpage=False,
    filename_template=None,
    filter_author=None,
    wp_custpost=False,
    wp_attach=False,
    attachments=None,
):

    pandoc_version = get_pandoc_version()
    posts_require_pandoc = []

    settings = read_settings()
    slug_subs = settings["SLUG_REGEX_SUBSTITUTIONS"]

    for (
        title,
        content,
        filename,
        date,
        author,
        categories,
        tags,
        status,
        kind,
        in_markup,
    ) in fields:
        if filter_author and filter_author != author:
            continue
        if is_pandoc_needed(in_markup) and not pandoc_version:
            posts_require_pandoc.append(filename)

        slug = not disable_slugs and filename or None

        if wp_attach and attachments:
            try:
                urls = attachments[filename]
                links = download_attachments(output_path, urls)
            except KeyError:
                links = None
        else:
            links = None

        ext = get_ext(out_markup, in_markup)
        if ext == ".md":
            header = build_markdown_header(
                title,
                date,
                author,
                categories,
                tags,
                slug,
                status,
                links.values() if links else None,
            )
        else:
            out_markup = "rst"
            header = build_header(
                title,
                date,
                author,
                categories,
                tags,
                slug,
                status,
                links.values() if links else None,
            )

        out_filename = get_out_filename(
            output_path,
            filename,
            ext,
            kind,
            dirpage,
            dircat,
            categories,
            wp_custpost,
            slug_subs,
        )
        print(out_filename)

        if in_markup in ("html", "wp-html"):
            html_filename = os.path.join(output_path, filename + ".html")

            with open(html_filename, "w", encoding="utf-8") as fp:
                # Replace newlines with paragraphs wrapped with <p> so
                # HTML is valid before conversion
                if in_markup == "wp-html":
                    new_content = decode_wp_content(content)
                else:
                    paragraphs = content.splitlines()
                    paragraphs = ["<p>{0}</p>".format(p) for p in paragraphs]
                    new_content = "".join(paragraphs)

                fp.write(new_content)

            if pandoc_version < (2,):
                parse_raw = "--parse-raw" if not strip_raw else ""
                wrap_none = "--wrap=none" if pandoc_version >= (1, 16) else "--no-wrap"
                cmd = (
                    "pandoc --normalize {0} --from=html" ' --to={1} {2} -o "{3}" "{4}"'
                )
                cmd = cmd.format(
                    parse_raw, out_markup, wrap_none, out_filename, html_filename
                )
            else:
                from_arg = "-f html+raw_html" if not strip_raw else "-f html"
                cmd = 'pandoc {0} --to={1}-smart --wrap=none -o "{2}" "{3}"'
                cmd = cmd.format(from_arg, out_markup, out_filename, html_filename)

            try:
                rc = subprocess.call(cmd, shell=True)
                if rc < 0:
                    error = "Child was terminated by signal %d" % -rc
                    exit(error)

                elif rc > 0:
                    error = "Please, check your Pandoc installation."
                    exit(error)
            except OSError as e:
                error = "Pandoc execution failed: %s" % e
                exit(error)

            os.remove(html_filename)

            with open(out_filename, "r", encoding="utf-8") as fs:
                content = fs.read()
                if out_markup == "markdown":
                    # In markdown, to insert a <br />, end a line with two
                    # or more spaces & then a end-of-line
                    content = content.replace("\\\n ", "  \n")
                    content = content.replace("\\\n", "  \n")

            if wp_attach and links:
                content = update_links_to_attached_files(content, links)

        with open(out_filename, "w", encoding="utf-8") as fs:
            fs.write(header + content)

    if posts_require_pandoc:
        logger.error(
            "Pandoc must be installed to import the following posts:"
            "\n  {}".format("\n  ".join(posts_require_pandoc))
        )

    if wp_attach and attachments and None in attachments:
        print("downloading attachments that don't have a parent post")
        urls = attachments[None]
        download_attachments(output_path, urls)


def main():
    parser = argparse.ArgumentParser(
        description="Transform feed, Blogger, Dotclear, Posterous, Tumblr, or"
        "WordPress files into reST (rst) or Markdown (md) files. "
        "Be sure to have pandoc installed.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(dest="input", help="The input file to read")
    parser.add_argument(
        "--blogger", action="store_true", dest="blogger", help="Blogger XML export"
    )
    parser.add_argument(
        "--dotclear", action="store_true", dest="dotclear", help="Dotclear export"
    )
    parser.add_argument(
        "--posterous", action="store_true", dest="posterous", help="Posterous export"
    )
    parser.add_argument(
        "--tumblr", action="store_true", dest="tumblr", help="Tumblr export"
    )
    parser.add_argument(
        "--wpfile", action="store_true", dest="wpfile", help="Wordpress XML export"
    )
    parser.add_argument(
        "--feed", action="store_true", dest="feed", help="Feed to parse"
    )
    parser.add_argument(
        "-o", "--output", dest="output", default="content", help="Output path"
    )
    parser.add_argument(
        "-m",
        "--markup",
        dest="markup",
        default="rst",
        help="Output markup format (supports rst & markdown)",
    )
    parser.add_argument(
        "--dir-cat",
        action="store_true",
        dest="dircat",
        help="Put files in directories with categories name",
    )
    parser.add_argument(
        "--dir-page",
        action="store_true",
        dest="dirpage",
        help=(
            'Put files recognised as pages in "pages/" sub-directory'
            " (blogger and wordpress import only)"
        ),
    )
    parser.add_argument(
        "--filter-author",
        dest="author",
        help="Import only post from the specified author",
    )
    parser.add_argument(
        "--strip-raw",
        action="store_true",
        dest="strip_raw",
        help="Strip raw HTML code that can't be converted to "
        "markup such as flash embeds or iframes (wordpress import only)",
    )
    parser.add_argument(
        "--wp-custpost",
        action="store_true",
        dest="wp_custpost",
        help="Put wordpress custom post types in directories. If used with "
        "--dir-cat option directories will be created as "
        "/post_type/category/ (wordpress import only)",
    )
    parser.add_argument(
        "--wp-attach",
        action="store_true",
        dest="wp_attach",
        help="(wordpress import only) Download files uploaded to wordpress as "
        "attachments. Files will be added to posts as a list in the post "
        "header. All files will be downloaded, even if "
        "they aren't associated with a post. Files will be downloaded "
        "with their original path inside the output directory. "
        "e.g. output/wp-uploads/date/postname/file.jpg "
        "-- Requires an internet connection --",
    )
    parser.add_argument(
        "--disable-slugs",
        action="store_true",
        dest="disable_slugs",
        help="Disable storing slugs from imported posts within output. "
        "With this disabled, your Pelican URLs may not be consistent "
        "with your original posts.",
    )
    parser.add_argument(
        "-e", "--email", dest="email", help="Email address (posterous import only)"
    )
    parser.add_argument(
        "-p", "--password", dest="password", help="Password (posterous import only)"
    )
    parser.add_argument(
        "-b", "--blogname", dest="blogname", help="Blog name (Tumblr import only)"
    )

    args = parser.parse_args()

    input_type = None
    if args.blogger:
        input_type = "blogger"
    elif args.dotclear:
        input_type = "dotclear"
    elif args.posterous:
        input_type = "posterous"
    elif args.tumblr:
        input_type = "tumblr"
    elif args.wpfile:
        input_type = "wordpress"
    elif args.feed:
        input_type = "feed"
    else:
        error = (
            "You must provide either --blogger, --dotclear, "
            "--posterous, --tumblr, --wpfile or --feed options"
        )
        exit(error)

    if not os.path.exists(args.output):
        try:
            os.mkdir(args.output)
        except OSError:
            error = "Unable to create the output folder: " + args.output
            exit(error)

    if args.wp_attach and input_type != "wordpress":
        error = "You must be importing a wordpress xml " "to use the --wp-attach option"
        exit(error)

    if input_type == "blogger":
        fields = blogger2fields(args.input)
    elif input_type == "dotclear":
        fields = dc2fields(args.input)
    elif input_type == "posterous":
        fields = posterous2fields(args.input, args.email, args.password)
    elif input_type == "tumblr":
        fields = tumblr2fields(args.input, args.blogname)
    elif input_type == "wordpress":
        fields = wp2fields(args.input, args.wp_custpost or False)
    elif input_type == "feed":
        fields = feed2fields(args.input)

    if args.wp_attach:
        attachments = get_attachments(args.input)
    else:
        attachments = None

    # init logging
    init()
    fields2pelican(
        fields,
        args.markup,
        args.output,
        dircat=args.dircat or False,
        dirpage=args.dirpage or False,
        strip_raw=args.strip_raw or False,
        disable_slugs=args.disable_slugs or False,
        filter_author=args.author,
        wp_custpost=args.wp_custpost or False,
        wp_attach=args.wp_attach or False,
        attachments=attachments or None,
    )
