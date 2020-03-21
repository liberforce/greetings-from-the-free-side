import logging

from pelican.settings import read_settings
from pelican.utils import SafeDatetime, slugify

import blog2pelican.parsers

logger = logging.getLogger(__name__)


class PosterousParser(blog2pelican.parsers.Parser):
    def __init__(self, api_token, email, password):
        self.api_token = api_token
        self.email = email
        self.password = password

    def _get_posterous_posts(self, page=1):
        import base64
        import json
        import urllib.request as urllib_request

        base64string = base64.encodestring(
            ("%s:%s" % (self.email, self.password)).encode("utf-8")
        ).replace("\n", "")
        url = (
            "http://posterous.com/api/v2/users/me/sites/primary/"
            "posts?api_token=%s&page=%d"
        ) % (self.api_token, page)
        request = urllib_request.Request(url)
        request.add_header("Authorization", "Basic %s" % base64string.decode())
        handle = urllib_request.urlopen(request)
        posts = json.loads(handle.read().decode("utf-8"))
        return posts

    def parse(self):
        """Imports posterous posts"""
        from datetime import timedelta

        page = 1
        posts = self._get_posterous_posts(page)
        settings = read_settings()
        subs = settings["SLUG_REGEX_SUBSTITUTIONS"]
        while len(posts) > 0:
            posts = self._get_posterous_posts(page)
            page += 1

            for post in posts:
                slug = post.get("slug")
                if not slug:
                    slug = slugify(post.get("title"), regex_subs=subs)
                tags = [tag.get("name") for tag in post.get("tags")]
                raw_date = post.get("display_date")
                date_object = SafeDatetime.strptime(
                    raw_date[:-6], "%Y/%m/%d %H:%M:%S"
                )
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
