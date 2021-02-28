class Renderer:
    file_ext = None

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
        raise NotImplementedError


class RendererFactory:
    @classmethod
    def from_markup(cls, in_markup, out_markup):
        if in_markup == "markdown" or out_markup == "markdown":
            from blog2pelican.renderers.markdown import MarkdownRenderer

            return MarkdownRenderer
        else:
            from blog2pelican.renderers.rst import RstRenderer

            return RstRenderer
