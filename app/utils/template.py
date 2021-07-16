# -*- coding: utf-8 -*-
'''
   Project:       puncSysDemo
   File Name:     template
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/7/15
   Software:      PyCharm
'''

'''定义模板渲染工具函数'''

# 开启jinja2的异步引擎
enable_async = True

'''
这里的PackageLoader接两个参数
    1. 模板html文件所在的文件夹，照着例中写即可，经测试影响不大
    2. 模板html文件实际所在的文件夹，建议相对路径，相对路径起始点为该文件所在位置
'''

import sys

from jinja2 import Environment, PackageLoader, select_autoescape
from sanic.response import html


env = Environment(
    loader=PackageLoader("app.templates", '../templates'),
    autoescape=select_autoescape(['html', 'xml', 'tpl']),
    enable_async=enable_async
    )

# 模板渲染工具函数，照抄
async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    rendered_template = await template.render_async(**kwargs)
    return html(rendered_template)
