#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'XiVO developers'
SITENAME = 'XiVO Blog'
SITEURL = ''
SITELOGO = 'public/xivo-logo.png'
FAVICON = SITEURL + '/public/favicon.ico'
COPYRIGHT_YEAR = '2015-2016'
CC_LICENSE = {'name': 'Create Commons Attribution-ShareAlike',
              'version': '4.0',
              'slug': 'by-sa'}


PATH = 'content'
THEME = 'themes/flex'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['public', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

MAIN_MENU = True

# Blogroll
LINKS = (
    ('XiVO.io', 'http://xivo.io'),
    ('Documentation', 'http://documentation.xivo.io'),
)

# Social widget
SOCIAL = (
    ('twitter', 'http://twitter.com/xivodevteam'),
    ('github', 'http://github.com/xivo-pbx'),
    ('facebook', 'https://www.facebook.com/XiVO-86529730831'),
)

MENUITEMS = (
    ('Categories', '/categories.html'),
    ('Archives', '/archives.html'),
)

DEFAULT_PAGINATION = 5
GOOGLE_ANALYTICS = 'UA-56722061-3'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
