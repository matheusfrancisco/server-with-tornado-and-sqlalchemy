import tornado.ioloop
from tornado import web
import tornado.web

from tornado_sqlalchemy import as_future, make_session_factory, SessionMixin
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.adapters.adpaters import FarmAdpater

from src.models.farm import Base as models_base
from tornado.options import define, options, parse_command_line


parse_command_line()

define("db_connection_str", default="postgres://postgres:postgres@localhost/development", help="Database connection string for application")
db_engine = create_engine(options.db_connection_str)
connection = db_engine.connect()
db_session = sessionmaker(bind=db_engine)
session = db_session()



class MyApplication(web.Application):

    def __init__(self, *args, **kwargs):
        self.session = kwargs.pop('session')
        self.session.configure(bind=db_engine)
        super(MyApplication, self).__init__(*args, **kwargs)


class ServerApp:
    @property
    def app(self):
        return self._app

    @app.setter
    def app(self, app):
        self._app = app

    def start(self):
        self.routers()
        models_base.metadata.create_all(db_engine)
        self.app.listen(8000)
        tornado.ioloop.IOLoop.instance().start()

    def routers(self):
        self.app = MyApplication([(r"/test", FarmAdpater, dict(db_session=db_session)), ], session=db_session)
