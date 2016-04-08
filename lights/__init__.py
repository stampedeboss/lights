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

settings = Settings()

# Create and engine and get the metadata
engine = create_engine('sqlite:///{}'.format(settings.DSN),
                       module=sqlite)
metadata = MetaData(bind=engine)
Session = sessionmaker(bind=engine, autocommit=True, expire_on_commit=False )

Base = declarative_base()
log.debug("DB Engine Initialized")


class Lights(object):

	logger.initialize(level=logging.DEBUG)

	settings = Settings()
	cmdoptions = CmdOptions()
	args = {}


	def __init__(self, **kwargs):

		super(Lights, self).__init__()
		return

if __name__ == '__main__':

	lights = Lights()
	sys.exit()

	pass
