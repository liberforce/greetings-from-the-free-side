#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from html import unescape

# because logging.setLoggerClass has to be called before logging.getLogger
from pelican.log import init  # noqa
from pelican.utils import SafeDatetime

from gandiblog2pelican.parsers.common import xml_to_soup, get_filename

logger = logging.getLogger(__name__)


def wp2fields(xml, wp_custpost=False):
    """Opens a wordpress XML file, and yield Pelican fields"""

    soup = xml_to_soup(xml)
    items = soup.rss.channel.findAll("item")
    for item in items:

        if item.find("status").string in ["publish", "draft"]:

            try:
                # Use HTMLParser due to issues with BeautifulSoup 3
                title = unescape(item.title.contents[0])
            except IndexError:
                title = "No title [%s]" % item.find("post_name").string
                logger.warning('Post "%s" is lacking a proper title', title)

            post_name = item.find("post_name").string
            post_id = item.find("post_id").string
            filename = get_filename(post_name, post_id)

            content = item.find("encoded").string
            raw_date = item.find("post_date").string
            if raw_date == u"0000-00-00 00:00:00":
                date = None
            else:
                date_object = SafeDatetime.strptime(
                    raw_date, "%Y-%m-%d %H:%M:%S"
                )
                date = date_object.strftime("%Y-%m-%d %H:%M")
            author = item.find("creator").string

            categories = [
                cat.string
                for cat in item.findAll("category", {"domain": "category"})
            ]

            tags = [
                tag.string
                for tag in item.findAll("category", {"domain": "post_tag"})
            ]
            # To publish a post the status should be 'published'
            status = (
                "published"
                if item.find("status").string == "publish"
                else item.find("status").string
            )

            kind = "article"
            post_type = item.find("post_type").string
            if post_type == "page":
                kind = "page"
            elif wp_custpost:
                if post_type == "post":
                    pass
                # Old behaviour was to name everything not a page as an
                # article.Theoretically all attachments have status == inherit
                # so no attachments should be here. But this statement is to
                # maintain existing behaviour in case that doesn't hold true.
                elif post_type == "attachment":
                    pass
                else:
                    kind = post_type
            yield (
                title,
                content,
                filename,
                date,
                author,
                categories,
                tags,
                status,
                kind,
                "wp-html",
            )
