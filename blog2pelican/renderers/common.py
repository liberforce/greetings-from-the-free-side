#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import re
import sys
from collections import defaultdict
from urllib.error import URLError
from urllib.parse import quote, urlparse, urlsplit, urlunsplit
from urllib.request import urlretrieve

from pelican.settings import read_settings
from pelican.utils import slugify

from blog2pelican import ProcessingStatus
from blog2pelican.repositories.common import get_filename, xml_to_soup
from blog2pelican.adapters.pandoc import PandocAdapter
from blog2pelican.renderers import RendererFactory

logger = logging.getLogger(__name__)


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

    out_filename = os.path.join(output_path, ".".join(filename, ext))
    # option to put page posts in pages/ subdirectory
    if dirpage and kind == "page":
        pages_dir = os.path.join(output_path, "pages")
        if not os.path.isdir(pages_dir):
            os.mkdir(pages_dir)
        out_filename = os.path.join(pages_dir, ".".join(filename, ext))
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
            output_path, typename, catname, ".".join(filename, ext),
        )
        if not os.path.isdir(os.path.join(output_path, typename, catname)):
            os.makedirs(os.path.join(output_path, typename, catname))
    # option to put files in directories with categories names
    elif dircat and (len(categories) > 0):
        catname = slugify(categories[0], regex_subs=slug_subs)
        out_filename = os.path.join(
            output_path, catname, ".".join(filename, ext),
        )
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


def fields2pelican(
    content,
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

    adapter = PandocAdapter()

    settings = read_settings()
    slug_subs = settings["SLUG_REGEX_SUBSTITUTIONS"]

    # Skip posts not written by a given author
    if filter_author and filter_author != content.author:
        content.processing_status = ProcessingStatus.SKIPPED
        return

    # Look for posts that require a markup conversion
    if adapter.supports(content.in_markup) and not adapter.available:
        content.processing_status = ProcessingStatus.FAILURE
        logger.warning(
            "{} is missing, failed to import: '{}'".format(
                adapter.name, content.filename,
            )
        )
        return

    content.slug = content.filename if not disable_slugs else None

    if wp_attach and attachments:
        try:
            urls = attachments[content.filename]
            links = download_attachments(output_path, urls)
        except KeyError:
            links = None
    else:
        links = None

    renderer_class = RendererFactory.from_markup(content.in_markup, out_markup)

    renderer = renderer_class(
        content.title,
        content.date,
        content.author,
        content.categories,
        content.tags,
        content.slug,
        content.status,
        links.values() if links else None,
    )
    header = renderer.render()

    out_filename = get_out_filename(
        output_path,
        content.filename,
        renderer.file_ext,
        content.kind,
        dirpage,
        dircat,
        content.categories,
        wp_custpost,
        slug_subs,
    )
    print(out_filename)

    output_content = adapter.adapt(
        content.in_markup,
        out_markup,
        output_path,
        content.filename,
        content.content,
        strip_raw,
        wp_attach,
        links,
        out_filename,
    )

    with open(out_filename, "w", encoding="utf-8") as fs:
        fs.write(header + output_content)

    content.processing_status = ProcessingStatus.SUCCESS
