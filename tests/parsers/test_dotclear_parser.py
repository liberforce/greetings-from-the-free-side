import blog2pelican.parsers.dotclear as parser


def test_simple():
    field_gen = parser.dc2fields("tests/data/simple.txt")
    fields = []
    for fieldset in field_gen:
        for field in fieldset:
            fields.append(field)

    assert fields[0] == "En direct d'Istanbul"  # title
    assert fields[1] == "post_content_xhtml"  # content
    assert fields[2] == "en-direct-distanbul"  # filename
    assert fields[3] == "2008-07-07 11:07"  # date
    assert fields[4] == "TEST-GANDI"  # author
    assert fields[5] == ["Life"]  # categories
    assert fields[6] == ["GUADEC", "GNOME"]  # tags
    assert fields[7] == "published"  # status
    assert fields[8] == "article"  # kind
    assert fields[9] == "html"  # format
