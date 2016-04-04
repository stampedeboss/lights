#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Purpose:

"""

import logging

__pgmname__ = '__init__.py'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class __init__(object):

	def __init__(self, id=None, **kwargs):
		log.trace('__init__.py.__init__')
		super(__init__.py, self).__init__()


if __name__ == '__main__':

	from sys import argv
	from lights import Lights
	from logging import DEBUG;

	TRACE = 5;
	VERBOSE = 15
	Lights.logger.initialize(level=DEBUG)

	Lights.args = Lights.cmdoptions.ParseArgs(argv[1:])
	Lights.logger.start(Lights.args.logfile, DEBUG, timed=Lights.args.timed)


	msg = "Prop: {}-{}, Controller: {} {} - {}/{}"

	# Create a session to use the tables
	session = create_session(bind=engine)

	controllers = session.query(Controller).filter(Connection.DisplayID == 1).all()
	# props = session.query(Prop).filter(Connection.DisplayID == 1).all()
	# q = session.query(Prop).all()

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
