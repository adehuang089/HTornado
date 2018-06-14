# -*- coding:utf-8 -*-

import tornado.web
import json


class IndexHandle(tornado.web.RequestHandler):
    def get(self):
        self.render('index/index.html')
        # self.write(json.dumps({"data": {"msg": '欢迎使用HTornado框架', "code": 200}}))
