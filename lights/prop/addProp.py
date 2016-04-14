#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
'''

import wx
import logging

from lights import Session, Product, Prop
from lights.GUI.lights import addProp as AP

__pgmname__ = 'addProp'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class addProp(AP):

	def __init__(self, parent):
		super(addProp, self).__init__(parent)
		self.parent = parent
		self.prodList = {}

		session = Session()
		prod = session.query(Product).all()
		for item in prod:
			entry = "{} {} {}".format(item.Style,
									 item.Protocol,
									 item.Details
									 )
			self.prodList[entry] = item.ID
			self.product.Append(entry)
		self.product.SetSelection(0)


	# Virtual event handlers, overide them in your derived class
	def addProp(self, event):
		new_props = []
		product = self.product.GetValue()
		productID = self.prodList[product]
		allocated = self.allocated.GetValue()
		units = self.units.GetValue()
		if allocated == 0:
			allocated = None
		if units == 0:
			units = None
		for i in range(self.start_number.GetValue(), self.units.GetValue() + 1):
			new_props.append({"Name" : self.name.GetValue(),
								"Unit": i,
								"Strings": self.strings.GetValue(),
								"Pixels": self.pixels.GetValue(),
								"PixelsAllocated": allocated,
								"ProductID": productID})

		self.parent.mdl.addItem(new_props)
		self.EndModal(0)

if __name__ == '__main__':
	from lights import Lights
	from sys import argv
	lights = Lights()
	lights.ParseArgs(argv[1:], trace=True)

	app = wx.App(False)
	d = addProp(None)
	d.Show()
	app.MainLoop()
