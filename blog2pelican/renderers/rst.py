import blog2pelican.renderers


class RstRenderer(blog2pelican.renderers.Renderer):
    def __init__(
        self,
        title,
        date,
        author,
        categories,
        tags,
        slug,
        status=None,
        attachments=None,
    ):
        self.title = title
        self.date = date
        self.author = author
        self.categories = categories
        self.tags = tags
        self.slug = slug
        self.status = status
        self.attachments = attachments

    def render(self):
        """Build a header from a list of fields"""

        from docutils.utils import column_width

        header = "%s\n%s\n" % (self.title, "#" * column_width(self.title))
        if self.date:
            header += ":date: %s\n" % self.date
        if self.author:
            header += ":author: %s\n" % self.author
        if self.categories:
            header += ":category: %s\n" % ", ".join(self.categories)
        if self.tags:
            header += ":tags: %s\n" % ", ".join(self.tags)
        if self.slug:
            header += ":slug: %s\n" % self.slug
        if self.status:
            header += ":status: %s\n" % self.status
        if self.attachments:
            header += ":attachments: %s\n" % ", ".join(self.attachments)
        header += "\n"
        return header
