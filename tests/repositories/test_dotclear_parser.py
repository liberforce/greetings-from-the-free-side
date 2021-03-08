from blog2pelican.repositories.dotclear import DotclearRepository


def test_simple():
    repo = DotclearRepository("tests/data/simple.txt")
    fields = []
    for fieldset in iter(repo):
        for field in fieldset:
            fields.append(field)

    assert fields[0] == "En direct d'Istanbul"  # title
    assert fields[1] == "<p>first paragraph</p>\\r<p>second paragraph</p>"  # content
    assert fields[2] == "en-direct-distanbul"  # filename
    assert fields[3] == "2008-07-07 11:07"  # date
    assert fields[4] == "TEST-GANDI"  # author
    assert fields[5] == ["Life"]  # categories
    assert fields[6] == ["GUADEC", "GNOME"]  # tags
    assert fields[7] == "published"  # status
    assert fields[8] == "article"  # kind
    assert fields[9] == "html"  # format
