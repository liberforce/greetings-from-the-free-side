#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import phpserialize

# because logging.setLoggerClass has to be called before logging.getLogger
from pelican.log import init  # noqa
from pelican.settings import read_settings
from pelican.utils import slugify

import blog2pelican.repositories


logger = logging.getLogger(__name__)


class DotclearRepository(blog2pelican.repositories.Repository):
    def __init__(self, filepath):
        self.filepath = filepath

    def _get_tags(self, post_meta, post_title=None):
        """
        Get tags related to a post
        """
        # Unclassified posts will get a special tag.
        # This will make it easier to find them afterwards.
        tags = ['Unclassified']

        # First, unescape characters that were escaped to store the data in
        # the backup file in CSV-like format
        post_meta = post_meta.replace("\\", "")
        if not post_meta:
            logger.debug("post has no metadata: '%s'", post_title)
            return tags

        tags_dict = phpserialize.loads(post_meta.encode("utf-8"))

        if not tags_dict:
            logger.debug("post has really no tags: '%s'", post_title)
            return tags

        if b"tag" not in tags_dict:
            logger.debug("post has no tags: '%s'", post_title)
            return tags

        tags = [tag.decode("utf-8") for tag in tags_dict[b"tag"].values()]

    def parse(self):
        """Opens a Dotclear export file, and yield pelican fields"""
        in_cat = False
        in_post = False
        category_list = {}
        posts = []

        with open(self.filepath, "r", encoding="utf-8") as f:
            for line in f:
                # remove final \n
                line = line[:-1]

                if line.startswith("[category"):
                    in_cat = True
                elif line.startswith("[post"):
                    in_post = True
                elif in_cat:
                    fields = line.split('","')
                    if not line:
                        in_cat = False
                    else:
                        # remove 1st and last ""
                        fields[0] = fields[0][1:]
                        # fields[-1] = fields[-1][:-1]
                        category_list[fields[0]] = fields[2]
                elif in_post:
                    if not line:
                        in_post = False
                        break
                    else:
                        posts.append(line)

        print("%i posts read." % len(posts))

        settings = read_settings()
        subs = settings["SLUG_REGEX_SUBSTITUTIONS"]
        for post in posts:
            fields = post.split('","')

            # post_id = fields[0][1:]
            # blog_id = fields[1]
            user_id = fields[2]
            cat_id = fields[3]
            post_dt = fields[4]
            # post_tz = fields[5]
            # post_creadt = fields[6]
            # post_upddt = fields[7]
            # post_password = fields[8]
            # post_type = fields[9]
            post_format = fields[10]
            # post_url = fields[11]
            # post_lang = fields[12]
            post_title = fields[13]
            post_excerpt = fields[14]
            post_excerpt_xhtml = fields[15]
            post_content = fields[16]
            post_content_xhtml = fields[17]
            # post_notes = fields[18]
            # post_words = fields[19]
            post_meta = fields[20]
            # post_status = fields[21]
            # post_selected = fields[22]
            # post_open_comment = fields[23]
            # post_open_tb = fields[24]
            # nb_comment = fields[25]
            # nb_trackback = fields[26]
            # post_position = fields[27]

            # remove seconds
            post_dt = ":".join(post_dt.split(":")[0:2])

            author = user_id

            tags = self._get_tags(post_meta, post_title)

            categories = []
            if cat_id:
                categories = [
                    category_list[id].strip() for id in cat_id.split(",")
                ]

            """
            dotclear2 does not use markdown by default unless
            you use the markdown plugin
            Ref: http://plugins.dotaddict.org/dc2/details/formatting-markdown
            """
            if post_format == "markdown":
                content = post_excerpt + post_content
            else:
                content = post_excerpt_xhtml + post_content_xhtml
                content = content.replace("\\n", "")
                post_format = "html"

            kind = "article"  # TODO: Recognise pages
            status = "published"  # TODO: Find a way for draft posts

            yield (
                post_title,
                content,
                slugify(post_title, regex_subs=subs),
                post_dt,
                author,
                categories,
                tags,
                status,
                kind,
                post_format,
            )
