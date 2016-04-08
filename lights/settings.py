#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Author: AJ Reynolds
Date: 01-29-2016
Purpose:
  Configuration and Run-time settings for the Lights

  Created by AJ Reynolds on %s.

"""

import logging
import os
import sys

from configobj import ConfigObj

__pgmname__ = "settings"

ConfigDir = os.path.join("~", ".config", "Lights")
ConfigDir = os.path.join("~")
ConfigFile = os.path.join(ConfigDir, "{}.cfg".format("Lights"))
ConfigFile = os.path.expanduser(ConfigFile)

if not os.path.exists(ConfigDir):
	os.makedirs(ConfigDir)

log = logging.getLogger(__pgmname__)

class Settings(object):
	"""
	Returns new Settings object with all settings from configuration file.

	settings: List of runtime information being requested.
	"""

	def __init__(self):

		if not os.path.exists(ConfigFile):
			self.build_config()
		self.load_config()

	def load_config(self):

		self.config = ConfigObj(ConfigFile, unrepr=True, interpolation=False)
		try:
			DB = self.config["DB"]
			self.Location = DB["Location"]
			self.FileName = DB["FileName"]
			self.DSN = os.path.join(self.Location, self.FileName)

		except Exception, e:
			log.warn("Configuration Setting Not Found, Rebuilding: {}".format(e))
			self.build_config()
			self.config.reset()
			self.load_config()

		return

	@staticmethod
	def build_config():

		config = ConfigObj(ConfigFile, unrepr=True, interpolation=False)

		config["DB"] = {}
		config["DB"]["Location"] = os.path.dirname(os.path.abspath(__file__))
		config["DB"]["FileName"] = "lights.sqlite"
		config.write()


if __name__ == '__main__':

	config = Settings()

	sys.exit(0)
