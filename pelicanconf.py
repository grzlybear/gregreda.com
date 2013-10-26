#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Greg Reda'
SITENAME = u'Greg Reda'
SITEURL = 'http://www.gregreda.com'
TIMEZONE = 'America/Chicago'
THEME = './theme/notebook-simpler'
SUMMARY_MAX_LENGTH = 50
AVATAR = '/theme/images/avatar.jpg'
TITLE = "Greg Reda: Data nerd in Chicago."
DESCRIPTION = "Greg Reda is a Chicagoan focused on analyzing data to provide insight and drive decisions. He also loves stats, visualization, beer, and music."

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'


# DEFAULTS
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'misc'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%d %b %Y'
DEFAULT_PAGINATION = False


# FEEDS
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"
TAG_FEED_ATOM = "feeds/tag/%s.atom.xml"


# PLUGINS
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = ['liquid_tags.notebook', 'liquid_tags.include_code',
            'liquid_tags.img', 'liquid_tags.video']

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'
EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

STATIC_PATHS = ['images', 'code', 'notebooks', 'extra']
EXTRA_PATH_METADATA = {'extra/robots.txt': {'path': 'robots.txt'},}


# Additional
DISQUS_SITENAME = "gregreda"
GOOGLE_ANALYTICS = "UA-34295039-1"
DOMAIN = "gregreda.com"