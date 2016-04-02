# -*- coding: UTF-8 -*-
'''
Purpose:

   Exceptions used through-out JET MSS

'''

__pgmname__     = 'exceptions'


class BaseLightsException(Exception):
    """Base exception all Lights exceptions
    """
    pass

# Configuration Exceptions
class ConfigError(BaseLightsException):
    """exception for config errors
    """
    pass

