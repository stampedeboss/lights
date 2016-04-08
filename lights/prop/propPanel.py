#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
'''

import wx
import logging
import wx.dataview as dv

from lights.GUI.lights import propFrame
from lights.prop.propmodel import propModel


__pgmname__ = 'props'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class Props(object):

	def __init__(self, data):
		super(Props, self).__init__()

		self.mdl = propModel(data)
		self.p = propFrame(None)
		self.p.prop_dataViewCtrl.AssociateModel(self.mdl)

		# Define the columns that we want in the view.  Notice the
		# parameter which tells the view which col in the data model to pull
		# values from for each view column.
		if 0:
			self.tr = tr = dv.DataViewTextRenderer()
			c0 = dv.DataViewColumn("ID",   # title
								   tr,        # renderer
								   0,         # data model column
								   width=80)
			self.p.prop_dataViewCtrl.AppendColumn(c0)
		else:
			self.p.prop_dataViewCtrl.AppendTextColumn("Name",   1, width=150)

		c1 = self.p.prop_dataViewCtrl.AppendTextColumn("Unit", 2, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c2 = self.p.prop_dataViewCtrl.AppendTextColumn("Strings", 3, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c3 = self.p.prop_dataViewCtrl.AppendTextColumn('Pixels', 4, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c4 = self.p.prop_dataViewCtrl.AppendTextColumn('Allocated', 5, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c5 = self.p.prop_dataViewCtrl.AppendTextColumn('Item', 6, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)

		c1.Alignment = wx.ALIGN_RIGHT
		c2.Alignment = wx.ALIGN_RIGHT
		c3.Alignment = wx.ALIGN_RIGHT
		c4.Alignment = wx.ALIGN_RIGHT
		c5.Alignment = wx.ALIGN_RIGHT

		# Set some additional attributes for all the columns
		for c in self.p.prop_dataViewCtrl.Columns:
			c.Sortable = True
			c.Reorderable = True


if __name__ == '__main__':
	from lights import Prop, Session

	app = wx.App(False)
	session = Session()
	session.begin()
	data = session.query(Prop).all()
	main = Props(data)
	main.p.Show()
	app.MainLoop()
	session.commit()