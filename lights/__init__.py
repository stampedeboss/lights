import logging
import sys
from sqlite3 import dbapi2 as sqlite

from sqlalchemy import create_engine

from cmdoptions import CmdOptions
from settings import Settings

__pgmname__ = 'lights'

log = logging.getLogger(__pgmname__)


class Lights(object):

	settings = Settings()
	options = CmdOptions()
	args = {}

	engine = create_engine('sqlite:///lights.sqlite', module=sqlite)
	log.debug("DB Engine Initialized")

	def __init__(self, **kwargs):

		super(Lights, self).__init__()
		return


if __name__ == '__main__':

	lights = Lights()
	sys.exit()

	pass
