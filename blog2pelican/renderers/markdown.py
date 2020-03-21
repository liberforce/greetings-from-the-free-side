import blog2pelican.renderers


class MarkdownRenderer(blog2pelican.renderers.Renderer):
    def render(self):
        """Build a header from a list of fields"""
        header = "Title: %s\n" % self.title
        if self.date:
            header += "Date: %s\n" % self.date
        if self.author:
            header += "Author: %s\n" % self.author
        if self.categories:
            header += "Category: %s\n" % ", ".join(self.categories)
        if self.tags:
            header += "Tags: %s\n" % ", ".join(self.tags)
        if self.slug:
            header += "Slug: %s\n" % self.slug
        if self.status:
            header += "Status: %s\n" % self.status
        if self.attachments:
            header += "Attachments: %s\n" % ", ".join(self.attachments)
        header += "\n"
        return header
