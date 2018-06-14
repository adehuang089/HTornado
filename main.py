#! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import os
from tornado.options import define, options
from core.url_handle import include, url_wrapper


class Application(tornado.web.Application):
    def __init__(self):
        # 定义 Tornado 服务器的配置项，如 static/templates 目录位置、debug 级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "public"),
            template_path=os.path.join(os.path.dirname(__file__), "app/view")
        )

        handlers = url_wrapper(include('route'))
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    print("Tornado server is start\r")
    define('port', default=8000, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    Application().listen(options.port, xheaders=True)
    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()

    print('Tornado server is stop')
