from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base
from sqlite3 import dbapi2 as sqlite

#Create and engine and get the metadata
Base = declarative_base()
engine = create_engine('sqlite:///lights.sqlite', module=sqlite)
metadata = MetaData(bind=engine)

#Reflect each database table we need to use, using metadata
class Prop(Base):
    __table__ = Table('Prop', metadata, autoload=True)

class Controller(Base):
    __table__ = Table('Controller', metadata, autoload=True)

class ControllerModels(Base):
    __table__ = Table('ControllerModels', metadata, autoload=True)

#Create a session to use the tables
session = create_session(bind=engine)

props = session.query(Prop).all()

print

for item in props:
    controller = session.query(Controller).filter_by(ControllerID=item.ControllerID).first()
    if not controller:
        print "Controller Name: {}, No Controller recorded".format(item.PropID)
    else:
        print "Controller Name: {}, Controller Model: {}".format(item.PropName, controller.Model)
