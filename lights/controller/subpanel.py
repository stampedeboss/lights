#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
'''

import wx
import logging
import wx.dataview as dv

from lights import Session, Controller
from lights.GUI.lights import subPanel as SP
from lights.controller.datamodel import dataModel
from lights.controller.addcontroller import addController

__pgmname__ = 'subpanel'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class subPanel(SP):

	def __init__(self, parent, frame):
		super(subPanel, self).__init__(parent)

		self.Title = u'Lights: Controllers'

		self.parent = parent
		self.frame = frame
		self.session = None
		self.data = None
		self.mdl = dataModel(self.data, self.session)
		self.dataViewCtrl.AssociateModel(self.mdl)

		# Define the columns that we want in the view.  Notice the
		# parameter which tells the view which col in the data model to pull
		# values from for each view column.
		self.tr = tr = dv.DataViewTextRenderer()
		c0 = dv.DataViewColumn("ID",  # title
		                       tr,  # renderer
		                       0,  # data model column
		                       width=50)
		self.dataViewCtrl.AppendColumn(c0)

		c1 = self.dataViewCtrl.AppendTextColumn("Name", 1, width=100, mode=dv.DATAVIEW_CELL_EDITABLE)
		c2 = self.dataViewCtrl.AppendTextColumn("IP", 2, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c3 = self.dataViewCtrl.AppendTextColumn("Univ", 3, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c4 = self.dataViewCtrl.AppendTextColumn('ModelID', 4, width=60, mode=dv.DATAVIEW_CELL_EDITABLE)
		c5 = self.dataViewCtrl.AppendTextColumn('Mfg', 5, width=100, mode=dv.DATAVIEW_CELL_INERT)
		c6 = self.dataViewCtrl.AppendTextColumn('Model', 6, width=100, mode=dv.DATAVIEW_CELL_INERT)
		c7 = self.dataViewCtrl.AppendTextColumn('Con', 7, width=35, mode=dv.DATAVIEW_CELL_INERT)

		c1.Alignment = wx.ALIGN_LEFT
		c2.Alignment = wx.ALIGN_CENTER
		c3.Alignment = wx.ALIGN_RIGHT
		c4.Alignment = wx.ALIGN_RIGHT
		c5.Alignment = wx.ALIGN_RIGHT
		c6.Alignment = wx.ALIGN_LEFT
		c7.Alignment = wx.ALIGN_LEFT

		# Set some additional attributes for all the columns
		for c in self.dataViewCtrl.Columns:
			c.Sortable = True
			c.Reorderable = True

		self.getData()
		return

	def getData(self):
		self.session = Session()
		self.data = self.session.query(Controller).all()
		self.mdl.session = self.session
		self.mdl.data = self.data
		self.mdl.Cleared()
		return

	# Handlers for subPanel events.
	# Handlers for subPanel events.
	def Exit(self, event):
		log.trace("Exit")
		self.frame.Close()

	def addItem(self, event):
		dlg = addController(self)
		dlg.ShowModal()
		dlg.Destroy()
		self.getData()
		self.Refresh()

	def delItem(self, event):
		if not self.dataViewCtrl.HasSelection():
			wx.MessageBox("Nothing selected, unable to delete", "Lights: Controller")
			return
		current = self.dataViewCtrl.GetSelection()
		self.mdl.delItem(current)
		self.getData()
		self.Refresh()


if __name__ == '__main__':
	from lights import Lights
	from sys import argv
	lights = Lights()
	lights.ParseArgs(argv[1:], test=True)

	from lights.GUI.lights import mainFrame

	app = wx.App(False)
	mf = mainFrame(None)
	sp = subPanel(mf.main_notebook, mf)
	mf.main_notebook.AddPage(sp, "Controller")
	mf.Show()
	app.MainLoop()