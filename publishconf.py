#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *
TIMEZONE = 'Asia/Shanghai'
SITEURL = ''
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = "synckey"
#GOOGLE_ANALYTICS = ""
DUOSHUO_SITENAME = u"synckey"
GOOGLE_ANALYTICS = "UA-55913313-1"
BAIDU_ANALYTICS = "1531ed173910c4c262dffb947842fe33"
