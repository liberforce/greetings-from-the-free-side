from blog2pelican.renderers.rst import RstRenderer


def test_rst_header():
    metadata = {
        "title": "My title",
        "date": "2020-03-21 03:00",
        "author": "TEST-GANDI",
        "categories": ["Life", "Computers"],
        "tags": ["Capitalized", "Tags"],
        "slug": "my-title",
    }
    renderer = RstRenderer(**metadata)
    header = renderer.render()
    assert (
        header
        == """My title
########
:date: 2020-03-21 03:00
:author: TEST-GANDI
:category: Life, Computers
:tags: Capitalized, Tags
:slug: my-title

"""
    )
