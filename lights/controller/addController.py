#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
'''

import wx
import logging

from lights import Session, Model, Controller, Connector
from lights.GUI.lights import addController as AC

__pgmname__ = 'addController'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class addController(AC):

	def __init__(self, parent):
		super(addController, self).__init__(parent)
		self.parent = parent
		self.modelList = {}

		session = Session()
		model = session.query(Model).all()
		for item in model:
			entry = "{} {}".format(item.Model,
									 item.Mfg
			                          )
			self.modelList[entry] = {"ID": item.ID,
			                         "Outputs": item.Outputs}
			self.model.Append(entry)
		self.model.SetSelection(0)


	# Virtual event handlers, overide them in your derived class
	def addItem(self, event):
		model = self.model.GetValue()
		modelID = self.modelList[model]["ID"]
		outputs = self.modelList[model]["Outputs"]
		new_ctlr = {"Name" : self.name.GetValue(),
					"IP_Address": self.ipaddr.GetValue(),
					"Universe": self.universe.GetValue(),
					"ModelID": modelID}

		self.parent.mdl.addItem(new_ctlr, outputs)
		self.EndModal(0)

if __name__ == '__main__':
	from lights import Lights
	from sys import argv
	lights = Lights()
	lights.ParseArgs(argv[1:], trace=True)

	app = wx.App(False)
	d = addController(None)
	d.Show()
	app.MainLoop()
