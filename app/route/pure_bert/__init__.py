# -*- coding: utf-8 -*-
'''
   Project:       puncSysDemo
   File Name:     __init__.py
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/7/15
   Software:      PyCharm
'''
from sanic import Blueprint

from app.route.pure_bert.index import frontend
from app.route.pure_bert.online_inference import inf

pure_bert = Blueprint.group(inf, frontend, url_prefix="/bert")
