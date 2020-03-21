def build_header(
    title, date, author, categories, tags, slug, status=None, attachments=None
):
    """Build a header from a list of fields"""

    from docutils.utils import column_width

    header = "%s\n%s\n" % (title, "#" * column_width(title))
    if date:
        header += ":date: %s\n" % date
    if author:
        header += ":author: %s\n" % author
    if categories:
        header += ":category: %s\n" % ", ".join(categories)
    if tags:
        header += ":tags: %s\n" % ", ".join(tags)
    if slug:
        header += ":slug: %s\n" % slug
    if status:
        header += ":status: %s\n" % status
    if attachments:
        header += ":attachments: %s\n" % ", ".join(attachments)
    header += "\n"
    return header
