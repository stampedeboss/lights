import logging
import sys

from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

from sqlite3 import dbapi2 as sqlite

from lights import logger
from cmdoptions import CmdOptions
from settings import Settings

__pgmname__ = 'lights'

log = logging.getLogger(__pgmname__)
Base = declarative_base()
Session = sessionmaker(autocommit=True, expire_on_commit=False )


class Lights(object):

	from lights import logger
	logger.initialize(level=logging.DEBUG)

	settings = Settings()
	cmdoptions = CmdOptions()
	args = {}

	log.debug("DB Engine Initialized")
	# Create and engine and get the metadata
	engine = create_engine('sqlite:///{}'.format(settings.DSN),
	                       module=sqlite)
	metadata = MetaData(bind=engine)
	Session.configure(bind=engine)

	def __init__(self, **kwargs):

		super(Lights, self).__init__()
		return

class CtlrModel(Base):
	__table__ = Table('CtlrModel', Lights.metadata, autoload=True)

class Controller(Base):
	__table__ = Table('Controller', Lights.metadata, autoload=True)
	model = relationship("CtlrModel", backref="controller")

class CtlrConnector(Base):
	__table__ = Table('CtlrConnector', Lights.metadata, autoload=True)
	controller = relationship("Controller", backref="connectors")
	connection = relationship("Connection",
							 backref=backref("connector", uselist=False))

class Display(Base):
	__table__ = Table('Display', Lights.metadata, autoload=True)

class Connection(Base):
	__table__ = Table('Connection', Lights.metadata, autoload=True)
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
	__table__ = Table('Prop', Lights.metadata, autoload=True)
	item = relationship("CatalogItem", backref="prop")
	propIn = relationship("Connection",
						  foreign_keys="Connection.Input_PropID",
						  backref=backref("input", uselist=False))
	propOut = relationship("Connection",
						   foreign_keys="Connection.Output_PropID",
						   backref=backref("output",uselist=False))

	#keywords = association_proxy('kw', 'keyword')

	def __init__(self):
		log.debug('prop.__init__')
		super(Prop, self).__init__()

		self.columns = Prop.__table__.columns.keys()


class CatalogItem(Base):
	__table__ = Table('CatalogItem', Lights.metadata, autoload=True)

if __name__ == '__main__':

	lights = Lights()
	sys.exit()

	pass
