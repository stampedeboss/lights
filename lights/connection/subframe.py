#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	This control provides these data columns:
		 0.  DisplayID:     integer
		 1.  DisplayName:   string
		 2.  ControllerName:string
		 3.  Connector:     integer
		 4.  TotalChannels: integer
		 5.  TotalPixels:   integer
		 6.  UniverseStart: integer
		 7.  UniverseEnd:   integer
		 8.  ChannelStart:  integer
		 9.  ChannelEnd:    integer
		 10. xLightStart:   integer
		 11. xLightEnd:     integer
'''

import wx
import logging
import wx.dataview as dv

from lights.GUI.lights import subFrame as SF
from lights.connection.datamodel import dataModel

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

		self.Title = u'Lights: Connections'
		self.mdl = None
		self.session = session
		self.mdl = dataModel(data, self.session)
		self.dataViewCtrl.AssociateModel(self.mdl)

		# Define the columns that we want in the view.  Notice the
		# parameter which tells the view which col in the data model to pull
		# values from for each view column.
		c0 = self.dataViewCtrl.AppendTextColumn("Display", 0, width=125, mode=dv.DATAVIEW_CELL_EDITABLE)
		c1 = self.dataViewCtrl.AppendTextColumn("Controller", 1, width=100, mode=dv.DATAVIEW_CELL_EDITABLE)
		c2 = self.dataViewCtrl.AppendTextColumn("Con", 2, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c3 = self.dataViewCtrl.AppendTextColumn('Chan', 3, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c4 = self.dataViewCtrl.AppendTextColumn('Pix', 4, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c5 = self.dataViewCtrl.AppendTextColumn('U S', 5, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c6 = self.dataViewCtrl.AppendTextColumn('U E', 6, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c7 = self.dataViewCtrl.AppendTextColumn('C S', 7, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c8 = self.dataViewCtrl.AppendTextColumn('C S', 8, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c9 = self.dataViewCtrl.AppendTextColumn('X S', 9, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)
		c10 = self.dataViewCtrl.AppendTextColumn('X E', 10, width=35, mode=dv.DATAVIEW_CELL_EDITABLE)

		c0.Alignment = wx.ALIGN_LEFT
		c1.Alignment = wx.ALIGN_LEFT
		c2.Alignment = wx.ALIGN_RIGHT
		c3.Alignment = wx.ALIGN_RIGHT
		c4.Alignment = wx.ALIGN_RIGHT
		c5.Alignment = wx.ALIGN_RIGHT
		c6.Alignment = wx.ALIGN_RIGHT
		c7.Alignment = wx.ALIGN_RIGHT
		c8.Alignment = wx.ALIGN_RIGHT
		c9.Alignment = wx.ALIGN_RIGHT
		c10.Alignment = wx.ALIGN_RIGHT

		# Set some additional attributes for all the columns
		for c in self.dataViewCtrl.Columns:
			c.Sortable = True
			c.Reorderable = True

		return

	# Handlers for subFrame events.
	def fileExit( self, event ):
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


if __name__ == '__main__':
	from lights import Lights
	from sys import argv
	lights = Lights()
	lights.ParseArgs(argv[1:], trace=True)

	from lights import Session, Connections

	app = wx.App(False)
	session = Session()
	data = session.query(Connections).all()
	sf = subFrame(None, data, session)
	sf.Show()
	app.MainLoop()
