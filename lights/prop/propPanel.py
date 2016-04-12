#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
'''

import wx
import logging
import wx.dataview as dv

from lights.GUI.lights import propFrame as PF
from lights.prop.propmodel import propModel
from lights import Session
from lights.prop import Prop

__pgmname__ = 'props'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class propFrame(PF):

	def __init__(self, parent):
		super(propFrame, self).__init__(parent)

		self.mdl = None
		self.session = None
		self.loadModel()

	def loadModel(self):

		self.session = Session()
		self.session.begin()
		data = self.session.query(Prop).all()
		self.mdl = propModel(data, self.session)
		self.prop_dataViewCtrl.AssociateModel(self.mdl)

		if 0:
			self.tr = tr = dv.DataViewTextRenderer()
			c0 = dv.DataViewColumn("ID",  # title
			                       tr,  # renderer
			                       0,  # data model column
			                       width=75)
			self.prop_dataViewCtrl.AppendColumn(c0)
		else:
			self.prop_dataViewCtrl.AppendTextColumn("Name", 1, width=150)

		c1 = self.prop_dataViewCtrl.AppendTextColumn("Unit", 2, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c2 = self.prop_dataViewCtrl.AppendTextColumn("Strings", 3, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c3 = self.prop_dataViewCtrl.AppendTextColumn('Pixels', 4, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c4 = self.prop_dataViewCtrl.AppendTextColumn('Allocated', 5, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c5 = self.prop_dataViewCtrl.AppendTextColumn('Item', 6, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)

		c1.Alignment = wx.ALIGN_RIGHT
		c2.Alignment = wx.ALIGN_RIGHT
		c3.Alignment = wx.ALIGN_RIGHT
		c4.Alignment = wx.ALIGN_RIGHT
		c5.Alignment = wx.ALIGN_RIGHT

		# Set some additional attributes for all the columns
		for c in self.prop_dataViewCtrl.Columns:
			c.Sortable = True
			c.Reorderable = True

		return


	# Handlers for propFrame events.
	def propExit(self, event):
		self.session.commit()
		self.Close()


	def addProp(self, event):
		# TODO: Implement addProp
		pass


	def delProp(self, event):
		# TODO: Implement delProp
		pass


	def saveProp(self, event):
		# TODO: Implement saveProp
		pass


	def refreshProp(self, event):
		self.mdl.Cleared()
		self.Refresh()
		print


if __name__ == '__main__':

	app = wx.App(False)
	pf = propFrame(None)
	pf.Show()
	app.MainLoop()
