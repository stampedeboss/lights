#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
"""
import logging
import logging.handlers
from logging import WARNING
import os
import re
import sys
import threading

from logging import INFO, DEBUG, ERROR, WARN
# A level more detailed than DEBUG
TRACE = 5
# A level more detailed than INFO
VERBOSE = 15

_logging_configured = False
_mem_handler = None
_logging_started = False


class MyLogger(logging.Logger):
    """ """
    local = threading.local()

    def trace(self, msg, *args, **kwargs):
        """Log at TRACE level (more detailed than DEBUG)."""
        self.log(TRACE, msg, *args, **kwargs)

    def verbose(self, msg, *args, **kwargs):
        """Log at VERBOSE level (displayed when FlexGet is run interactively.)"""
        self.log(VERBOSE, msg, *args, **kwargs)

    # backwards compatibility
    debugall = trace


class PrivacyFilter(logging.Filter):
    """Edits log messages and <hides> obviously private information."""

    def __init__(self):
        super(logging.Filter, self).__init__()

        self.replaces = []

        def hide(name):
            s = '([?&]%s=)\w+' % name
            p = re.compile(s)
            self.replaces.append(p)

        for param in ['passwd', 'password', 'pw', 'pass', 'passkey',
            'key', 'apikey', 'user', 'username', 'uname', 'login', 'id']:
            hide(param)

    def filter(self, record):
        if not isinstance(record.msg, basestring):
            return False
        for p in self.replaces:
            record.msg = p.sub(r'\g<1><hidden>', record.msg)
            record.msg = record.msg
        return False


class Whitelist(logging.Filter):
    def __init__(self, *whitelist):
        self.whitelist = [logging.Filter(name) for name in whitelist]

    def filter(self, record):
        _process = any(f.filter(record) for f in self.whitelist)
        for f in self.whitelist:
            value = f.filter(record)
        return _process

    def modify(self,*whitelist):
        self.whitelist = [logging.Filter(name) for name in whitelist]


class Blacklist(Whitelist):

    def __init__(self):
        super(logging.Filter, self).__init__()

    def filter(self, record):
        return not Whitelist.filter(self, record)


def initialize(unit_test=False, level=TRACE, console=True):
    """Prepare logging.
    """
    global _logging_configured, _mem_handler

    if _logging_configured:
        return

    logging.addLevelName(TRACE, 'TRACE')
    logging.addLevelName(VERBOSE, 'VERBOSE')
    _logging_configured = True

    # root logger
    log = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    _mem_handler = logging.handlers.MemoryHandler(1000 * 1000, 100)
    _mem_handler.setFormatter(formatter)
    log.addHandler(_mem_handler)

    if console:
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        console.set_name('Console')
        log.addHandler(console)

    if unit_test:
        log.setLevel(level)
        return

    if '--trace' in sys.argv:
        log.setLevel(TRACE)
    elif '--debug-trace' in sys.argv:
        log.setLevel(TRACE)
    elif '--debug' in sys.argv:
        log.setLevel(logging.DEBUG)
    elif '--verbose' in sys.argv:
        log.setLevel(VERBOSE)
    elif '--quiet' in sys.argv:
        log.setLevel(logging.WARNING)
    elif '--errors' in sys.argv:
        log.setLevel(logging.ERROR)
    elif '--critical' in sys.argv:
        log.setLevel(logging.CRITICAL)
    else:
        log.setLevel(logging.INFO)


def start(filename='default.log', level=logging.INFO, timed=False, errorlog=False):
    """After initialization, start file logging.
    """
    global _logging_started

    assert _logging_configured
    if _logging_started:
        return

    if timed:
        handler = logging.handlers.TimedRotatingFileHandler(filename, when='midnight', backupCount=9)
    else:
        handler = logging.handlers.RotatingFileHandler(filename, backupCount=9)
        handler.doRollover()

    handler.set_name('Main')
    handler.setFormatter(_mem_handler.formatter)

    _mem_handler.setTarget(handler)

    if errorlog:
        _error_log_dir = os.path.dirname(filename)
        _error_filename = os.path.splitext(os.path.basename(filename))[0]+'.error'+os.path.splitext(os.path.basename(filename))[1]
        _error_log = os.path.join(_error_log_dir, _error_filename)
        error_handler = logging.handlers.RotatingFileHandler(_error_log, maxBytes=1000 * 1024, backupCount=9)
        error_handler.doRollover()
        error_handler.set_name('Error')

    # root logger
    log = logging.getLogger()
    log.removeHandler(_mem_handler)
    log.addHandler(handler)
    log.addFilter(PrivacyFilter())
    log.setLevel(level)
    if errorlog:
        log.addHandler(error_handler)
        error_handler.setLevel(WARNING)

    # flush what we have stored from the plugin initialization
    _mem_handler.flush()
    _logging_started = True

def flush_logging_to_console():
    """Flushes memory logger to console"""
    console = logging.StreamHandler()
    console.setFormatter(_mem_handler.formatter)
    log = logging.getLogger()
    log.addHandler(console)
    if len(_mem_handler.buffer) > 0:
        for record in _mem_handler.buffer:
            console.handle(record)
    _mem_handler.flush()

# Set our custom logger class as default
logging.setLoggerClass(MyLogger)
