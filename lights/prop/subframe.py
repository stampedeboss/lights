#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
'''

import wx
import logging
import wx.dataview as dv

from lights.GUI.lights import subFrame as SF
from lights.prop.datamodel import dataModel

__pgmname__ = 'subframe'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class subFrame(SF):

	def __init__(self, parent, data, session):
		super(subFrame, self).__init__(parent)
		log.trace("__init__")

		self.Title = u'Lights: Props'
		self.mdl = None
		self.session = session
		self.mdl = dataModel(data, self.session)
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

		c1 = self.dataViewCtrl.AppendTextColumn("Name", 1, width=125, mode=dv.DATAVIEW_CELL_EDITABLE)
		c2 = self.dataViewCtrl.AppendTextColumn("Unit", 2, width=50, mode=dv.DATAVIEW_CELL_EDITABLE)
		c3 = self.dataViewCtrl.AppendTextColumn("Strings", 3, width=50, mode=dv.DATAVIEW_CELL_EDITABLE)
		c4 = self.dataViewCtrl.AppendTextColumn('Pixels', 4, width=50, mode=dv.DATAVIEW_CELL_EDITABLE)
		c5 = self.dataViewCtrl.AppendTextColumn('Allocated', 5, width=60, mode=dv.DATAVIEW_CELL_EDITABLE)
		c6 = self.dataViewCtrl.AppendTextColumn('Product', 6, width=75, mode=dv.DATAVIEW_CELL_ACTIVATABLE)

		c1.Alignment = wx.ALIGN_LEFT
		c2.Alignment = wx.ALIGN_RIGHT
		c3.Alignment = wx.ALIGN_RIGHT
		c4.Alignment = wx.ALIGN_RIGHT
		c5.Alignment = wx.ALIGN_RIGHT
		c6.Alignment = wx.ALIGN_LEFT

		# Set some additional attributes for all the columns
		for c in self.dataViewCtrl.Columns:
			c.Sortable = True
			c.Reorderable = True

		return


	# Handlers for subFrame events.
	def fileExit( self, event ):
		log.trace("fileExit")
		self.Close()

	def addItem( self, event ):
		# TODO: Implement addProp
		pass

	def delItem( self, event ):
		# TODO: Implement delProp
		pass

	def saveRecs( self, event ):
		# TODO: Implement saveProp
		pass

	def refreshDB( self, event ):
		#self.mdl.Cleared()
		self.Show()
		print


if __name__ == '__main__':
	from lights import Lights
	from sys import argv
	lights = Lights()
	lights.ParseArgs(argv[1:], trace=True)

	from lights import Session, Props

	app = wx.App(False)
	session = Session()
	q = session.query(Props).all()
	sf = subFrame(None, q, session)
	sf.Show()
	app.MainLoop()
