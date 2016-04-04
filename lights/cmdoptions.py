#!/usr/bin/env python
# encoding: utf-8
'''
cmd_options -- Command Line Options Handler for JET MSS

'''
import os
import sys
import logging
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

from os.path import dirname, expanduser, join, split, splitext, isabs
from subprocess import Popen, PIPE
from sys import argv, exit

import logger

__pgmname__ = os.path.splitext(os.path.basename(argv[0]))[0]

log = logging.getLogger(__pgmname__)

try:
	_p = Popen(["git", "describe", "HEAD", "--long", "--tags"],
			   cwd=dirname(dirname(__file__)),
			   stdout=PIPE)
	__version__ = _p.communicate()[0].strip('\n').strip()
except Exception, e:
	log.error("Could not get revision number: {}".format(e))
	__version__ = 'Unknown'

try:
	_p = Popen(["git", "log", "-1", "--format=%cd", "--date=local"],
			   cwd=dirname(dirname(__file__)),
			   stdout=PIPE)
	__commit_date__ = _p.communicate()[0].strip('\n').strip()
except Exception, e:
	log.error("Could not get commit date: {}".format(e))
	__commit_date__ = 'Unknown'

_p = None

program_version_message = '%%(prog)s %s (%s)' % (__version__, __commit_date__)
program_license = '''

Created by AJ Reynolds.
Copyright 2016 AJ Reynolds. All rights reserved.

Licensed under the Creative Commons Zero (CC0) License

Distributed on an "AS IS" basis without warranties
or conditions of any kind, either express or implied.

USAGE
'''

class CmdOptions(ArgumentParser):
	'''Define Standard Options for All Command lines.'''
	def __init__(self, **kwargs):

		super(CmdOptions, self).__init__(self, **kwargs)

		self.parser = ArgumentParser(description=program_license,
									 formatter_class=RawDescriptionHelpFormatter,
									 conflict_handler='resolve')
		self.parser.add_argument('-V', '--version',
								 action='version',
								 version=program_version_message)
		self.parser.add_argument('--logdir', action='store',
								 dest='logdir', default='/srv/log',
								 help='Specify a log directory [default: %(default)s]')
		self.parser.add_argument('--logfile', action='store',
								 dest='logfile',
                                 default=os.path.splitext(os.path.basename(argv[0]))[0] + '.log',
								 help='Specify a custom logfile filename [default: %(default)s]')
		self.parser.add_argument("--Error-Log", dest="errorlog", action="store_true", default=False,
								 help="Create Seperate Log for Errors")
		self.parser.add_argument('--session_log', dest="session_log",
		                         action="store_false", default=True,
		                         help="paths to folder(s) with config file(s) ")
		self.parser.add_argument('pathname', metavar="pathname", nargs='*',
								 help="paths to folder(s)/file(s) ")  # Setup argument parser

		group_loglvl = self.parser.add_mutually_exclusive_group()
		group_loglvl.add_argument("--verbose", dest="loglevel",
						action="store_const", const="VERBOSE",
						default='INFO',
						help="increase logging to include additional informational information")
		group_loglvl.add_argument("--debug", dest="loglevel",
						action="store_const", const="DEBUG",
						help="increase logging to include debugging information")
		group_loglvl.add_argument("--trace", dest="loglevel",
						action="store_const", const="TRACE",
						help="increase logging to include trace information")
		group_loglvl.add_argument("--quiet", dest="loglevel",
						action="store_const", const="WARNING",
						help="Limit logging to only include Warning, Errors, and Critical information")
		group_loglvl.add_argument("--errors", dest="loglevel",
						action="store_const", const="ERROR",
						help="Limit logging to only include Errors and Critical information")

	def ParseArgs(self, arg):

		args = self.parser.parse_args(arg)
		log.debug("Parsed command line: {!s}".format(args))

		log_level = logger.logging.getLevelName(args.loglevel.upper())
		log_file = os.path.expanduser(args.logfile)

		# If an absolute path is not specified, use the default directory.
		if not os.path.isabs(log_file):
			log_file = os.path.join(os.path.expanduser("~/"), log_file)

		logger.start(log_file, log_level, timed=args.session_log)

		return args


if __name__ == "__main__":

	logger.initialize()

	opt = CmdOptions()
	args = opt.parser.parse_args(argv[1:])
	log.info(args)
	exit(0)
