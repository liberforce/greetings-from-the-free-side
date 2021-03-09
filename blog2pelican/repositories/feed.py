import logging
import time

from pelican.settings import read_settings
from pelican.utils import slugify

import blog2pelican

logger = logging.getLogger(__name__)


class FeedRepository(blog2pelican.repositories.Repository):
    def __init__(self, filepath):
        self.filepath = filepath

    def parse(self):
        """Read a feed and yield pelican fields"""
        import feedparser

        d = feedparser.parse(self.filepath)
        settings = read_settings()
        subs = settings["SLUG_REGEX_SUBSTITUTIONS"]
        for entry in d.entries:
            date = (
                time.strftime("%Y-%m-%d %H:%M", entry.updated_parsed)
                if hasattr(entry, "updated_parsed")
                else None
            )
            author = entry.author if hasattr(entry, "author") else None
            tags = (
                [e["term"] for e in entry.tags]
                if hasattr(entry, "tags")
                else None
            )

            slug = slugify(entry.title, regex_subs=subs)
            kind = "article"
            yield blog2pelican.entities.content.Content(
                title=entry.title,
                content=entry.description,
                slug=slug,
                date=date,
                author=author,
                categories=[],
                tags=tags,
                status=None,
                kind=kind,
                markup="html",
            )
