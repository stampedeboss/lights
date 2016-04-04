from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import create_session
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import contains_eager, joinedload

from sqlite3 import dbapi2 as sqlite
from datetime import datetime


dsn = '/home/aj/PycharmProjects/Lights/Lights/Lights.sqlite'
#Create and engine and get the metadata
Base = declarative_base()
engine = create_engine('sqlite:////{}'.format(dsn), module=sqlite)
metadata = MetaData(bind=engine)

class CtlrModel(Base):
	__table__ = Table('CtlrModel', metadata, autoload=True)

class Controller(Base):
	__table__ = Table('Controller', metadata, autoload=True)
	model = relationship("CtlrModel", backref="controller")

class CtlrConnector(Base):
	__table__ = Table('CtlrConnector', metadata, autoload=True)
	controller = relationship("Controller", backref="connectors")
	connection = relationship("Connection",
							 backref=backref("connector", uselist=False))

class Display(Base):
	__table__ = Table('Display', metadata, autoload=True)

class Connection(Base):
	__table__ = Table('Connection', metadata, autoload=True)
	display = relationship("Display", backref="connection")
	# propIn = relationship("Prop",
	# 					  foreign_keys="Connection.Input_PropID",
	# 					  backref=backref("input", uselist=False))
	# propOut = relationship("Prop",
	# 					   foreign_keys="Connection.Output_PropID",
	# 					   backref=backref("output",uselist=False))
	# connector = relationship("CtlrConnector",
	# 					   backref=backref("connection", uselist=False))


class Prop(Base):
	__table__ = Table('Prop', metadata, autoload=True)
	item = relationship("CatalogItem", backref="prop")
	propIn = relationship("Connection",
						  foreign_keys="Connection.Input_PropID",
						  backref=backref("input", uselist=False))
	propOut = relationship("Connection",
						   foreign_keys="Connection.Output_PropID",
						   backref=backref("output",uselist=False))

	#keywords = association_proxy('kw', 'keyword')


class CatalogItem(Base):
	__table__ = Table('CatalogItem', metadata, autoload=True)


if __name__ == '__main__':

	msg = "Prop: {}-{}, Controller: {} {} - {}/{}"

	#Create a session to use the tables
	session = create_session(bind=engine)

	controllers = session.query(Controller).filter(Connection.DisplayID == 1).all()
	#props = session.query(Prop).filter(Connection.DisplayID == 1).all()
	#q = session.query(Prop).all()

	for item in q:
		if item.PixelsAllocated:
			allocated = item.Strings * item.PixelsAllocated
		else:
			allocated = item.Strings * item.Pixels
		'''
		if item.controllers:
			for controller in item.controllers:
				print msg.format(item.Name,
								 item.Version,
								 controller.controller.Name,
								 controller.controller.model.Model,
								 item.Strings,
								 allocated
								 )
		else:
		'''
		print msg.format(item.Name,
							 item.Version,
							 "UNASSIGNED",
							 "",
							 item.Strings,
							 allocated
							 )
