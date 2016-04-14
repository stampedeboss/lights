#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	----------------------------------------------------------------------
	This model acts as a bridge between the DataViewCtrl and the displays and Controller data

	This model provides these data columns:

		 0. DisplayName:    string
		 1. ControllerID    integer
		 2. Sequence        integer
		 3. ControllerName  string
		 4. ControllerMfg   string
		 5. ControllerModel string
		 6. ModelID         integer
		 7. IP_Address      integer
		 8. Universe        integer
'''

import wx
import logging
import wx.dataview as dv

from lights import DisplayController, Display, Controller

__pgmname__ = 'datamodel'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class dataModel(dv.PyDataViewModel):

	def __init__(self, data, session):
		super(dataModel, self).__init__()
		self.data = data
		self.session = session
		self.objmapper.UseWeakRefs(True)

		self.displays = []

		self.type = {0: 'integer'}
		for i in range(1, self.GetColumnCount()):
			self.type[i] = 'string'
		log.trace("displaycontroller.datamodel Initialization Complete")

	def GetColumnCount(self):
		# Report how many columns this model provides data for.
		log.trace("GetColumnCount")
		return 9

	def GetColumnType(self, col):
		# Map the data column numbers to the data type
		log.trace("GetColumnType")
		return self.type[col]

	def IsContainer(self, item):
		# Return True if the item has children, False otherwise.
		# The hidden root is a container
		log.trace("IsContainer")
		if not item:
			return True
		return False

	def GetParent(self, item):
		# Return the item which is this item's parent.
		log.trace("GetParent")

		if not item:
			return dv.NullDataViewItem

		node = self.ItemToObject(item)
		if isinstance(node, Display):
			return dv.NullDataViewItem
		elif isinstance(node, DisplayController):
			for g in self.data:
				if g.DisplayID == node.ID:
					return self.ObjectToItem(g.display)

	def GetChildren(self, parent, children):
		# The view calls this method to find the children of any node in the
		# control. There is an implicit hidden root node, and the top level
		# item(s) should be reported as children of this node. A List view
		# simply provides all items as children of this hidden root. A Tree
		# view adds additional items as children of the other items, as needed,
		# to provide the tree hierachy.

		# If the parent item is invalid then it represents the hidden root
		# item, so we'll use the display objects as its children and they will
		# end up being the collection of visible roots in our tree.
		log.trace("GetChildren")
		if not self.data:
			return 0

		displays = []
		if not parent:
			for entry in self.data:
				if entry.DisplayID in displays:
					continue
				children.append(self.ObjectToItem(entry.display))
				displays.append(entry.DisplayID)
			return len(displays)

		# Otherwise we'll fetch the python object associated with the parent
		# item and make DV items for each of it's child objects.
		node = self.ItemToObject(parent)
		if isinstance(node, Display):
			for ctlr in self.data:
				if ctlr.DisplayID == node.ID:
					children.append(self.ObjectToItem(ctlr.controller))
			return len(self.data)
		return 0

	def GetValue(self, item, col):
		# Return the value to be displayed for this item and column.
		log.trace("GetValue")

		mapper = {0: None}
		for i in range(1, self.GetColumnCount()):
			mapper[i] = None

		node = self.ItemToObject(item)
		if isinstance(node, Display):
			mapper[0] = node.DisplayName
			return mapper[col]
		if isinstance(node, DisplayController):
			mapper = {  0: node.display.DisplayName,
						1: node.ControllerID,
						2: node.Sequence,
						3: node.controller.ControllerName,
						4: node.controller.model.ControllerMfg,
						5: node.controller.model.ControllerModel,
						6: node.controller.ModelID,
						7: node.controller.IP_Address,
						8: node.controller.Universe
			          }
			return mapper[col]
		else:
			raise RuntimeError("unknown node type")

	def SetValue(self, value, item, col):
		# We're not allowing edits in column zero
		log.trace("SetValue: %s" % value)

		node = self.ItemToObject(item)
		if isinstance(node, DisplayController):
			self.session.begin(subtransactions=True)
			if col == 2:
				node.Sequence = value
			self.session.commit()

	def addItem(self, item):
		self.session.begin(subtransactions=True)
		new_display = DisplayController(**item)
		self.session.add(new_display)
		self.session.flush()
		self.session.commit()

	def delItem(self, item):
		node = self.ItemToObject(item)
		self.session.begin(subtransactions=True)
		self.session.delete(node)
		self.session.commit()


if __name__ == '__main__':
	from lights import Lights
	from sys import argv
	lights = Lights()
	lights.ParseArgs(argv[1:], test=True)

	from lights import Session

	app = wx.App(False)
	# Create a session to use the tables
	session = Session()
	q = session.query(DisplayController).all()

	mdl = dataModel(q, session)
	print mdl
