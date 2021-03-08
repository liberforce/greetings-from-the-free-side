import logging
import os

from pelican.utils import SafeDatetime

import blog2pelican
from blog2pelican.repositories.common import xml_to_soup

logger = logging.getLogger(__name__)


class BloggerRepository(blog2pelican.repositories.Repository):
    def __init__(self, filepath):
        self.filepath = filepath

    def parse(self):
        """Opens a blogger XML file, and yield Pelican fields"""
        soup = xml_to_soup(self.filepath)
        entries = soup.feed.findAll("entry")
        for entry in entries:
            raw_kind = entry.find(
                "category", {"scheme": "http://schemas.google.com/g/2005#kind"}
            ).get("term")
            if raw_kind == "http://schemas.google.com/blogger/2008/kind#post":
                kind = "article"
            elif (
                raw_kind
                == "http://schemas.google.com/blogger/2008/kind#comment"
            ):
                kind = "comment"
            elif (
                raw_kind == "http://schemas.google.com/blogger/2008/kind#page"
            ):
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
                date_object = SafeDatetime.strptime(
                    raw_date[:23], "%Y-%m-%dT%H:%M:%S.%f"
                )
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

            yield (
                title,
                content,
                filename,
                date,
                author,
                None,
                tags,
                status,
                kind,
                "html",
            )
