import tornado.ioloop
import tornado.web

from src.adapters.adpaters import Adpaters, AboutHandler


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", Adpaters),
        (r"/about", AboutHandler)])
    app.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
