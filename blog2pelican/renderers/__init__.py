class Renderer:
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
