import tornado.ioloop
import tornado.web


class Adpaters(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Xicao")
