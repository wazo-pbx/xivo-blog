#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'The Wazo Authors'
SITENAME = 'Wazo Blog'
SITEURL = 'http://blog.wazo.community'
SITELOGO = 'public/wazo-logo.png'
COPYRIGHT_YEAR = '2016'
CC_LICENSE = {'name': 'Create Commons Attribution-ShareAlike',
              'version': '4.0',
              'slug': 'by-sa'}


PATH = 'content'
THEME = 'themes/flex'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'en'

ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['public']

MAIN_MENU = True

# Blogroll
LINKS = (
    ('Wazo Website', 'http://wazo.community'),
    ('Documentation', 'http://documentation.wazo.community'),
)

# Social widget
SOCIAL = (
    ('twitter', 'http://twitter.com/wazocommunity'),
    ('github', 'http://github.com/wazo-pbx'),
)

MENUITEMS = (
    ('Categories', '/categories.html'),
    ('Archives', '/archives.html'),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
