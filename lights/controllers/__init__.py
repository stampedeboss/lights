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

__pgmname__ = 'controller'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class Controller(Base):
	__table__ = Table('Controller', metadata, autoload=True)
	#model = relationship("CtlrModel", backref="controller")

	def __init__(self):
		log.debug('prop.__init__')
		super(Controller, self).__init__()

		self.columns = Controller.__table__.columns.keys()
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


class CatalogItem(Base):
	__table__ = Table('CatalogItem', metadata, autoload=True)


if __name__ == '__main__':
	from lights import Lights, Session

	table = Controller()
	# Create a session to use the tables
	session = Session()
	db = session.query(Controller).all()
	print db

