import json

from tornado import web, gen
import tornado.ioloop
import tornado.web

from tornado.options import define, options, parse_command_line
from src.models.farm import FarmAsyncModel, Farm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class FarmAdpater(tornado.web.RequestHandler):

    def initialize(self, db_session):
        self.db = db_session
        self.farm_model = FarmAsyncModel(db_session)

    @web.asynchronous
    @gen.coroutine
    def put(self):
        obj = json.loads(self.request.body)
        done = yield gen.Task(self.farm_model.update_by_id, obj)
        self.write("Updated")


    @web.asynchronous
    @gen.coroutine
    def delete(self):
        id_ = json.loads(self.request.body)
        done = yield gen.Task(self.farm_model.delete, int(id_["id"]))
        self.write("Deleted")

    @web.asynchronous
    @gen.coroutine
    def get(self):
        id_ = json.loads(self.request.body)
        done = yield gen.Task(self.farm_model.get_by_id, int(id_["id"]))
        self.write(done.to_json())

    @web.asynchronous
    @gen.coroutine
    def post(self):
        posted_data = json.loads(self.request.body.decode('utf-8'))
        value = Farm(name=posted_data.get("name"), latitude=posted_data.get("latitude"), longitude=posted_data.get("longitude"))
        done = yield gen.Task(self.farm_model.create, value)
        self.write("Created")
