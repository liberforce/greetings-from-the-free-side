import logging

from pelican.settings import read_settings
from pelican.utils import SafeDatetime, slugify


logger = logging.getLogger(__name__)


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
