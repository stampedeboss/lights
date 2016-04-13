#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
'''

import wx
import logging
import wx.dataview as dv

from lights import Session, Display
from lights.GUI.lights import subPanel as SP
from lights.display.datamodel import dataModel

__pgmname__ = 'subframe'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class subPanel(SP):

	def __init__(self, parent):
		super(subPanel, self).__init__(parent)

		self.Title = u'Lights: Display'
		self.parent = parent
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
		                       width=80)
		self.dataViewCtrl.AppendColumn(c0)

		c1 = self.dataViewCtrl.AppendTextColumn("Name", 1, width=125, mode=dv.DATAVIEW_CELL_EDITABLE)
		c1.Alignment = wx.ALIGN_LEFT

		# Set some additional attributes for all the columns
		for c in self.dataViewCtrl.Columns:
			c.Sortable = True
			c.Reorderable = True

		self.getData()
		return

	def getData(self):
		self.session = Session()
		self.data = self.session.query(Display).all()
		self.mdl.session = self.session
		self.mdl.data = self.data
		self.mdl.Cleared()
		return

	# Handlers for subPanel events.
	def Exit( self, event ):
		self.Close()

	def addItem(self, event):
		dlg = wx.TextEntryDialog(
			self, 'What is name of the Display?',
			'Lights: Add Display', '')

		if dlg.ShowModal() == wx.ID_OK:
			log.debug('Add new Display: %s\n' % dlg.GetValue())
			self.mdl.addItem({"DisplayName": dlg.GetValue()})

		dlg.Destroy()
		self.getData()
		self.Refresh()

	def delItem( self, event ):
		if not self.dataViewCtrl.HasSelection():
			wx.MessageBox("Nothing selected, unable to delete", "Lights: Display")
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
	sp = subPanel(mf.main_notebook)
	mf.main_notebook.AddPage(sp, "Displays")
	mf.Show()
	app.MainLoop()