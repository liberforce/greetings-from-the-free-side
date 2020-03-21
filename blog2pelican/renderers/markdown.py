def build_markdown_header(
    title, date, author, categories, tags, slug, status=None, attachments=None
):
    """Build a header from a list of fields"""
    header = "Title: %s\n" % title
    if date:
        header += "Date: %s\n" % date
    if author:
        header += "Author: %s\n" % author
    if categories:
        header += "Category: %s\n" % ", ".join(categories)
    if tags:
        header += "Tags: %s\n" % ", ".join(tags)
    if slug:
        header += "Slug: %s\n" % slug
    if status:
        header += "Status: %s\n" % status
    if attachments:
        header += "Attachments: %s\n" % ", ".join(attachments)
    header += "\n"
    return header
