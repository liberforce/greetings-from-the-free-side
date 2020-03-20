import sys


def xml_to_soup(xml):
    """Opens an xml file"""
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        error = (
            'Missing dependency "BeautifulSoup4" and "lxml" required to '
            "import XML files."
        )
        sys.exit(error)
    with open(xml, encoding="utf-8") as infile:
        xmlfile = infile.read()
    soup = BeautifulSoup(xmlfile, "xml")
    return soup


def get_filename(post_name, post_id):
    if post_name is None or post_name.isspace():
        return post_id
    else:
        return post_name
