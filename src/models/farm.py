import json

from sqlalchemy import Integer, Column, String, Numeric
from tornado.gen import coroutine
from tornado.concurrent import return_future, run_on_executor
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.web import Application, RequestHandler
from concurrent.futures import ThreadPoolExecutor


from tornado_sqlalchemy import (
    SessionMixin,
    as_future,
    declarative_base,
    make_session_factory,
)

Base = declarative_base()

EXECUTOR = ThreadPoolExecutor(20)


class Farm(Base):
    __tablename__ = 'farm'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    latitude = Column(Numeric)
    longitude = Column(Numeric)

    def to_json(self):
        return({'name': self.name, 'latitude': str(self.latitude), 'longitude': str(self.longitude)})


class FarmAsyncModel:
    def __init__(self, db_session, io_loop=None, executor=EXECUTOR):
        self.io_loop = io_loop or IOLoop.instance()
        self.db_session = db_session

    def get_by_id(self, id: int, callback=None):
        session = self.db_session()
        result = session.query(Farm).filter(Farm.id==id).one()
        session.close()
        callback(result)

    def create(self, farm_orm, callback=None):
        session = self.db_session()
        success = True
        try:
            session.add(farm_orm)
            session.commit()
        except Exception as e:
            session.rollback()
            success = e
        session.close()
        callback(success)

    def update_by_id(self, data_to_update, callback=None):
        session = self.db_session()
        farm = session.query(Farm).filter(Farm.id == int(data_to_update.get("id")))
        data = {"name": data_to_update.get("name"),
                "latitude": data_to_update.get("latitude"),
                "longitude": data_to_update.get("longitude")}
        farm.update(data)
        session.commit()
        callback(farm)

    def delete(self, id: int, callback=None):
        session = self.db_session()
        result = session.query(Farm).filter(Farm.id==id).first()
        session.delete(result)
        session.commit()
        session.close()
        callback(result)
