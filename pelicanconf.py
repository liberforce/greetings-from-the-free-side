#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "liberforce"
SITENAME = "Greetings From The Free Side!"
SITEURL = "blog.freeside.fr"

PATH = "content"
STATIC_PATHS = ["media"]

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "fr"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("GNOME", "http://www.gnome.org"),
    ("Mageia", "http://www.mageia.org"),
)

# Social widget
SOCIAL = (
    ("Mastodon", "https://framapiaf.org/@liberforce"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# File location
ARTICLE_URL = 'post/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

# Plugins
PLUGIN_PATHS = ["../pelican-plugins"]
PLUGINS = ["neighbors"]
