#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	----------------------------------------------------------------------
	This model acts as a bridge between the DataViewCtrl and the Prop data, and
	organizes it hierarchically as a collection of Props.

	This model provides these data columns:

		 0. ID:      integer
		 1. Name:    string
		 2. Version: string
		 3. Strings: integer
		 4. Pixels:  integer
		 5. Allocated: Integer
'''

import wx
import logging
import wx.dataview as dv

from lights import Prop


__pgmname__ = 'propmodel'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class propModel(dv.PyDataViewModel):

	def __init__(self, data):
		super(propModel, self).__init__()
		self.data = data
		self.objmapper.UseWeakRefs(True)

	def GetColumnCount(self):
		# Report how many columns this model provides data for.
		log.debug("GetColumnCount")
		return 7

	def GetColumnType(self, col):
		# Map the data column numbers to the data type
		log.debug("GetColumnType")
		mapper = {0: 'integer',
				  1: 'string',
				  2: 'integer',
				  3: 'integer',
				  4: 'integer',
				  5: 'integer',
				  6: 'integer'
				  }
		return mapper[col]

	def IsContainer(self, item):
		# Return True if the item has children, False otherwise.
		# The hidden root is a container
		log.debug("IsContainer")
		if not item:
			return True
		return False

	def GetParent(self, item):
		log.debug("GetParent\n")
		return dv.NullDataViewItem

	def GetChildren(self, parent, children):
		# The view calls this method to find the children of any node in the
		# control. If the parent item is invalid then it represents the hidden root
		# item, so we'll use the genre objects as its children and they will
		# end up being the collection of visible roots in our tree.
		log.debug("GetChildren")
		if not parent:
			for item in self.data:
				children.append(self.ObjectToItem(item))
			return len(self.data)
		return 0

	def GetValue(self, item, col):
		# Return the value to be displayed for this item and column.
		log.debug("GetValue")

		node = self.ItemToObject(item)
		if isinstance(node, Prop):
			if node.PixelsAllocated:
				allocated = node.PixelsAllocated
			else:
				allocated = node.Strings * node.Pixels
			mapper = {0: node.ID,
					  1: node.Name,
					  2: node.Version,
					  3: node.Strings,
					  4: node.Pixels,
					  5: allocated,
					  6: node.CatalogItemID
					  }
			return mapper[col]
		else:
			raise RuntimeError("unknown node type")

	def SetValue(self, value, item, col):
		# We're not allowing edits in column zero
		log.debug("SetValue: %s" % value)

		node = self.ItemToObject(item)
		if isinstance(node, Prop):
			if col == 1:
				node.Name = value
			elif col == 2:
				node.Version = value
			elif col == 3:
				node.Strings = value
			elif col == 4:
				node.Pixels = value
			elif col == 5:
				node.PixelsAllocated = value
			elif col == 6:
				node.CatalogItemID = value

	def AddProp(self):
		prop = Prop()

if __name__ == '__main__':
	from lights import Session

	app = wx.App(False)
	# Create a session to use the tables
	session = Session()
	props = session.query(Prop).all()

	mdl = propModel(props)
	print mdl

# main = MyFrame4(None)
#	main.m_notebook3.AddPage(myGrid(main.m_notebook3), "Props")
#	main.Show()
#	app.MainLoop()

