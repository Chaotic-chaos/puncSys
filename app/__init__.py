# -*- coding: utf-8 -*-
'''
   Project:       puncSysDemo
   File Name:     __init__.py
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/7/15
   Software:      PyCharm
'''

# 初始化app
from sanic import Sanic
from sanic_cors import CORS

from app.route.pure_bert import pure_bert


def create_app():
    app = Sanic(__name__)

    CORS(app)

    # 注册蓝图
    app.blueprint(pure_bert)

    return app
