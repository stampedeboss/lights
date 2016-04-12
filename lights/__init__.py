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


class Products(Base):
	__table__ = Table('Product', metadata, autoload=True)

	def __init__(self):
		log.debug('CatlogItems.__init__')
		super(Products, self).__init__()

		self.columns = Products.columns.keys()

class CtlrModels(Base):
	__table__ = Table('CtlrModel', metadata, autoload=True)

	def __init__(self):
		log.debug('CtlrModels.__init__')
		super(CtlrModels, self).__init__()

		self.columns = CtlrModels.__table__.columns.keys()


class Displays(Base):
	__table__ = Table('Display', metadata, autoload=True)

	def __init__(self):
		log.debug('Displays.__init__')
		super(Displays, self).__init__()

		self.columns = Displays.__table__.columns.keys()


class Controllers(Base):
	__table__ = Table('Controller', metadata, autoload=True)
	model = relationship("CtlrModels", backref=backref("controllers"))

	def __init__(self):
		log.debug('Controllers.__init__')
		super(Controllers, self).__init__()

		self.columns = Controllers.__table__.columns.keys()


class Connectors(Base):
	__table__ = Table('Connector', metadata, autoload=True)
	controller = relationship("Controllers", backref="connectors")

	def __init__(self):
		log.debug('CtlrConnectors.__init__')
		super(CtlrConnectors, self).__init__()

		self.columns = CtlrConnectors.__table__.columns.keys()


class Connections(Base):
	__table__ = Table('Connection', metadata, autoload=True)
	display = relationship("Displays", backref="connections")
	connector = relationship("Connectors", backref=backref("connection", uselist=False))
	propIn = relationship("Props", foreign_keys="Connections.Input_PropID",
						  backref=backref("input", uselist=False))
	propOut = relationship("Props", foreign_keys="Connections.Output_PropID",
						   backref=backref("output", uselist=False))

	def __init__(self):
		log.debug('Connections.__init__')
		super(Connections, self).__init__()

		self.columns = Connections.__table__.columns.keys()


class Props(Base):
	__table__ = Table('Prop', metadata, autoload=True)
	product = relationship("Products", backref="prop")

	#keywords = association_proxy('kw', 'keyword')

	def __init__(self):
		log.debug('prop.__init__')
		super(Prop, self).__init__()

		self.columns = Prop.__table__.columns.keys()


if __name__ == '__main__':
	from sys import argv
	lights = Lights()
	lights.ParseArgs(argv[1:], test=True)

	# Create a session to use the tables
	session = Session()
	models = session.query(CtlrModels).all()
	controllers = session.query(Controllers).all()
	connectors = session.query(Connectors).all()
	connections = session.query(Connections).all()
	displays = session.query(Displays).all()
	products = session.query(Products).all()
	props = session.query(Props).all()

	for item in props:
		log.info("Prop ID: {} {} {}".format(item.ID, item.Name, item.Unit))

	log.info(props)

	sys.exit()
