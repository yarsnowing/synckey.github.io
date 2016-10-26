#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'andy'
SITENAME = u"Andy's Blog"
SITEURL = ''
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'en'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MD_EXTENSIONS = (['codehilite(css_class=github)'])

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 30

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
#DISQUS_SITENAME = u"synckey"
DUOSHUO_SITENAME = u"synckey"
THEME = "pelican-bootstrap3"
HIDE_SIDEBAR = True
# BOOTSTRAP_FLUID =  True
# PDF_PROCESSOR = True
PYGMENTS_STYLE = "github"

STATIC_PATHS = ['static', 'static/images/favicon.ico']
#ARTICLE_PATHS = ['posts']
EXTRA_PATH_METADATA = {
    "static/images/favicon.ico": {"path": "favicon.ico"},
 #   "static/baidu_verify_eO5agZyv5R.html": {"path": "baidu_verify_eO5agZyv5R.html"},
}

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL

DISPLAY_CATEGORIES_ON_MENU = False

PLUGIN_PATHS = ["plugins"]
PLUGINS = ["neighbors", "bootstrapify"]

DEFAULT_WECHAT_PIC = "wechat_logo_300x300.jpg"
