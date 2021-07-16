# -*- coding: utf-8 -*-
'''
   Project:       puncSysDemo
   File Name:     index
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/7/15
   Software:      PyCharm
'''
from sanic import Blueprint, text

from app.utils.template import template

'''前端页面路由'''

frontend = Blueprint("frontend")
frontend.static("/statics", "app/static/pure_bert")


@frontend.route("/index")
async def index(request):
    return await template("pure_bert/index.html")
