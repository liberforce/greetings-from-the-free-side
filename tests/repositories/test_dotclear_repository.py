from blog2pelican.repositories.dotclear import DotclearRepository
from blog2pelican.entities.content import Content


def test_simple():
    repo = DotclearRepository("tests/data/repositories/dotclear/simple.txt")
    content = next(iter(repo))

    expected = Content(
        title="En direct d'Istanbul",
        content="<p>first paragraph</p>\\r<p>second paragraph</p>",
        slug="en-direct-distanbul",
        date="2008-07-07 11:07",
        author="TEST-GANDI",
        categories=["Life"],
        tags=["GUADEC", "GNOME"],
        status="published",
        kind="article",
        post_format="html",
    )

    assert content == expected
