# -*- coding: utf-8 -*-
'''
   Project:       puncSysDemo
   File Name:     run
   Author:        Chaos
   Email:         life0531@foxmail.com
   Date:          2021/7/15
   Software:      PyCharm
'''
# 启动入口
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
