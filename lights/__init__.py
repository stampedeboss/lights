import logging
import os, sys

from sqlalchemy import create_engine, MetaData, Table, event
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy

from sqlite3 import dbapi2 as sqlite

from lights import logger
from cmdoptions import CmdOptions
from settings import Settings

__pgmname__ = 'lights'

log = logging.getLogger(__pgmname__)

settings = Settings()

Base = declarative_base()

# Create and engine and get the metadata
engine = create_engine('sqlite:///{}'.format(settings.DSN), module=sqlite)
metadata = MetaData(bind=engine)
Session = sessionmaker(bind=engine, autocommit=True, expire_on_commit=False )
log.debug("DB Engine Initialized")


class Lights(object):

	logger.initialize(level=logging.DEBUG)
	settings = Settings()
	cmdoptions = CmdOptions()
	args = {}


	def __init__(self, log_level=None, **kwargs):

		super(Lights, self).__init__()
		return


	def ParseArgs(self, arg, test=None, trace=False):
		Lights.args = Lights.cmdoptions.parser.parse_args(arg)

		Lights.args.logfile = os.path.expanduser(Lights.args.logfile)
		# If an absolute path is not specified, use the default directory.
		if not os.path.isabs(Lights.args.logfile):
			if os.path.exists(Lights.args.logdir):
				Lights.args.logfile = os.path.join(Lights.args.logdir, Lights.args.logfile)
			else:
				Lights.args.logfile = os.path.join(os.path.expanduser("~/"), Lights.args.logfile)

		log_level = logger.logging.getLevelName(Lights.args.loglevel.upper())
		if test:  log_level = logger.DEBUG
		if trace: log_level = logger.TRACE
		logger.start(Lights.args.logfile, log_level, timed=Lights.args.session_log)
		log.debug("Parsed command line: {!s}".format(Lights.args))


class Product(Base):
	__table__ = Table('Product', metadata, autoload=True)

	def __init__(self, **kwargs):
		log.debug('CatlogItems.__init__')
		super(Product, self).__init__(**kwargs)


class Model(Base):
	__table__ = Table('Model', metadata, autoload=True)

	def __init__(self, **kwargs):
		log.debug('CtlrModel.__init__')
		super(Model, self).__init__(**kwargs)


class Display(Base):
	__table__ = Table('Display', metadata, autoload=True)

	def __init__(self, **kwargs):
		log.debug('Display.__init__')
		super(Display, self).__init__(**kwargs)


class Controller(Base):
	__table__ = Table('Controller', metadata, autoload=True)
	model = relationship("Model", backref="controllers")

	def __init__(self, **kwargs):
		log.debug('Controller.__init__')
		super(Controller, self).__init__(**kwargs)


class DisplayController(Base):
	__table__ = Table('DisplayController', metadata, autoload=True)
	display = relationship("Display", backref="controllers")
	controller = relationship("Controller", backref="displays")

	def __init__(self, **kwargs):
		log.debug('DisplayController.__init__')
		super(DisplayController, self).__init__(**kwargs)


class Connector(Base):
	__table__ = Table('Connector', metadata, autoload=True)
	controller = relationship("Controller", backref="connectors")

	def __init__(self, **kwargs):
		log.debug('Connector.__init__')
		super(Connector, self).__init__(**kwargs)


class Connection(Base):
	__table__ = Table('Connection', metadata, autoload=True)
	display = relationship("Display", backref="connections")
	connector = relationship("Connector", backref=backref("connections"))
	propIn = relationship("Prop", foreign_keys="Connection.Input_PropID",
						  backref=backref("inputs"))
	propOut = relationship("Prop", foreign_keys="Connection.Output_PropID",
						   backref=backref("outputs"))

	def __init__(self, **kwargs):
		log.debug('Connection.__init__')
		super(Connection, self).__init__(**kwargs)


class Prop(Base):
	__table__ = Table('Prop', metadata, autoload=True)
	product = relationship("Product", backref="prop")

	#keywords = association_proxy('kw', 'keyword')

	def __init__(self, **kwargs):
		log.debug('prop.__init__')
		super(Prop, self).__init__(**kwargs)


if __name__ == '__main__':
	from sys import argv
	lights = Lights()
	lights.ParseArgs(argv[1:], test=True)

	# Create a session to use the tables
	session = Session()
	models = session.query(Model).all()
	controllers = session.query(Controller).all()
	connectors = session.query(Connector).all()
	connections = session.query(Connection).all()
	displays = session.query(Display).all()
	dispctlrs = session.query(DisplayController).all()
	products = session.query(Product).all()
	props = session.query(Prop).all()

	for item in props:
		log.info("Prop ID: {} {} {}".format(item.ID, item.Name, item.Unit))

	log.info(props)

	sys.exit()
