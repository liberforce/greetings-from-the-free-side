from blog2pelican.parsers.dotclear import DotclearParser


def test_simple():
    parser = DotclearParser("tests/data/simple.txt")
    field_gen = parser.parse()
    fields = []
    for fieldset in field_gen:
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
