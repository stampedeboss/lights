import logging
from lights import Lights
from lights.exceptions import ConfigError

from sqlalchemy import Table, select, MetaData

__pgmname__ = 'Prop'
log = logging.getLogger(__pgmname__)

class Prop(object):

	def __init__(self, **kwargs):

		log.debug("Prop: Initialize Started")
		super(Prop, self).__init__()

		self.PropID = None

		self.load_attr(kwargs)

		return

	def load_attr(self, kwargs):
		if len(kwargs) > 0:
			for key, val in kwargs.items():
				if val is unicode:
					setattr(self, key, val).encode('ascii', 'ignore')
				else:
					setattr(self, key, val)
		return

	def list(self):

		props = []
		metadata = MetaData()

		try:
			tbl_prop = Table('Prop', metadata,
			             autoload=True,
			             autoload_with=Lights.engine)
			con = Lights.engine.connect()
		except Exception, e:
			log.warn("Could not connect to the database: {}".format(e))
			return

		stm = select([tbl_prop])

		try:
			for row in con.execute(stm):
				props.append(Prop(**row))
		except Exception, e:
			log.error("Unable to retrieve Props: {}".format(e))
			return

		return props

	def copy(self):
		_new_prop = Prop()
		for key, val in self.__dict__.iteritems():
			if val is not None:
				setattr(_new_prop, key, val)
		return _new_prop

	def __str__(self):
		"""Return a string representation of a :class:`Movie`"""
		header = '<PROP>'
		header = map(str, header)
		header = ' '.join(header)
		return '{}: {}'.format(header, self.PropID)

	__repr__ = __str__


if __name__ == '__main__':

	from sys import argv
	from datetime import datetime

	from lights import Lights
	from lights import logger

	logger.initialize()
	Lights.args = Lights.options.ParseArgs(argv[1:])

	prop = Prop()
	props = prop.list()
	log.info('Props: {}'.format(props))
