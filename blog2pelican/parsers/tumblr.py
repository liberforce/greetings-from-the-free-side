import logging

from pelican.settings import read_settings
from pelican.utils import SafeDatetime, slugify


logger = logging.getLogger(__name__)


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
                SafeDatetime.fromtimestamp(int(timestamp)).strftime(
                    "%Y-%m-%d-"
                )
                + slug
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
                        % (
                            photo.get("caption"),
                            photo.get("original_size").get("url"),
                        )
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
