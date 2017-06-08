# coding=utf8

import sys
import web

from config import config


class WebServer(object):

    def __init__(self):
        self.urls = (
            '/', 'select',
            '/delete', 'delete'
        )

    def startServer(self):
        sys.argv.append('0.0.0.0:%s' % config.PORT)
        app = web.application(self.urls, globals())
        app.run()


class select(object):

    def GET(self):
        return 'get'

    def POST(self):
        return 'post'


class delete(object):

    def GET(self):
        return 'get'

    def POST(sefl):
        return 'post'

server = WebServer()
