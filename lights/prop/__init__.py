#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	----------------------------------------------------------------------
	This model acts as a bridge between the DataViewCtrl and the Prop data, and
	organizes it hierarchically as a collection of Props.

	This model provides these data columns:

		 0. ID:      integer
		 1. Name:    string
		 2. Version: string
		 3. Strings: integer
		 4. Pixels:  integer
		 5. Allocated: Integer
'''

import logging
import sys

from sqlalchemy import Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy

from lights import Base, metadata

__pgmname__ = 'prop'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class Prop(Base):
	__table__ = Table('Prop', metadata, autoload=True)
	# item = relationship("CatalogItem", backref="prop")
	# propIn = relationship("Connection",
	# 					  foreign_keys="Connection.Input_PropID",
	# 					  backref=backref("input", uselist=False))
	# propOut = relationship("Connection",
	# 					   foreign_keys="Connection.Output_PropID",
	# 					   backref=backref("output",uselist=False))

	#keywords = association_proxy('kw', 'keyword')

	def __init__(self):
		log.debug('prop.__init__')
		super(Prop, self).__init__()

		self.columns = Prop.__table__.columns.keys()

if __name__ == '__main__':
	from lights import Lights, Session

	# Create a session to use the tables
	session = Session()
	props = session.query(Prop).all()
	print props

