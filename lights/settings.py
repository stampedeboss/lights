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

ConfigDir = os.path.join("~", ".config", "lights")
ConfigDir = os.path.join("~")
ConfigFile = os.path.join(ConfigDir, "{}.cfg".format("lights"))
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
			Lights = self.config["Lights"]

			Log_Message = self.config["Log_Message"]
			self.Queue_Depth            = Log_Message["Queue_Depth"]
		except Exception, e:
			log.warn("Configuration Setting Not Found, Rebuilding: {}".format(e))
			self.build_config()
			self.config.reset()
			self.load_config()

		return

	@staticmethod
	def build_config():

		config = ConfigObj(ConfigFile, unrepr=True, interpolation=False)

		config["Lights"] = {}

		config["Log_Message"] = {}
		config["Log_Message"]["Queue_Depth"]          = "Current Queue Depth: {}"

		config.write()


if __name__ == '__main__':

	config = Settings()

	sys.exit(0)
