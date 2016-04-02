#!/usr/bin/env python
# encoding: utf-8
'''
cmd_options -- Command Line Options Handler for JET MSS

'''
import os
import sys
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter

import logger

__pgmname__ = os.path.splitext(os.path.basename(sys.argv[0]))[0]

log = logger.logging.getLogger(__pgmname__)

class CmdOptions(ArgumentParser):
    '''Define Standard Options for All Command lines.'''
    def __init__(self, **kwargs):

        super(CmdOptions, self).__init__(self, **kwargs)

        args = ''

        # Setup argument parser
        self.parser = ArgumentParser(formatter_class=RawDescriptionHelpFormatter,
                        conflict_handler='resolve')
        self.parser.add_argument('--logfile', action='store', nargs='?',
                        dest='logfile', default='JETMSS.log',
                        help='Specify a custom logfile filename [default: %(default)s]')
        self.parser.add_argument('--config', metavar="config", nargs='?',
                        help="paths to folder(s) with config file(s) ")
        self.parser.add_argument('--session_log', dest="session_log",
                        action="store_false", default=True,
                        help="paths to folder(s) with config file(s) ")

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
    args = opt.parser.parse_args(sys.argv[1:])
    log.info(args)
    sys.exit(0)
