# -*- coding: utf-8 -*-
# @Author: Du Jun

from scrapy.cmdline import execute
import sys,os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
execute(['scrapy','crawl','hx'])