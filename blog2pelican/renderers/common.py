#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import re
import subprocess
import sys
from collections import defaultdict
from urllib.error import URLError
from urllib.parse import quote, urlparse, urlsplit, urlunsplit
from urllib.request import urlretrieve

from pelican.settings import read_settings
from pelican.utils import slugify

from blog2pelican.renderers.rst import RstRenderer
from blog2pelican.renderers.markdown import build_markdown_header
from blog2pelican.parsers.common import get_filename, xml_to_soup
from blog2pelican.parsers.wordpress import decode_wp_content

logger = logging.getLogger(__name__)


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
        out_filename = os.path.join(
            output_path, typename, catname, filename + ext
        )
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
                (
                    item.find("post_parent").string,
                    item.find("attachment_url").string,
                )
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
            renderer = RstRenderer(
                title,
                date,
                author,
                categories,
                tags,
                slug,
                status,
                links.values() if links else None,
            )
            header = renderer.render()

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
                wrap_none = (
                    "--wrap=none" if pandoc_version >= (1, 16) else "--no-wrap"
                )
                cmd = (
                    "pandoc --normalize {0} --from=html"
                    ' --to={1} {2} -o "{3}" "{4}"'
                )
                cmd = cmd.format(
                    parse_raw,
                    out_markup,
                    wrap_none,
                    out_filename,
                    html_filename,
                )
            else:
                from_arg = "-f html+raw_html" if not strip_raw else "-f html"
                cmd = 'pandoc {0} --to={1}-smart --wrap=none -o "{2}" "{3}"'
                cmd = cmd.format(
                    from_arg, out_markup, out_filename, html_filename
                )

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
