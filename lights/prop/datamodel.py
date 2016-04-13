#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	----------------------------------------------------------------------
	This model acts as a bridge between the DataViewCtrl and the Prop data, and
	organizes it hierarchically as a collection of Prop.

	This model provides these data columns:

		 0. ID:      integer
		 1. Name:    string
		 2. Version: string
		 3. Strings: integer
		 4. Pixels:  integer
		 5. Allocated: Integer
		 6. CtlrModelID: Integer
'''

import wx
import logging
import wx.dataview as dv

from lights import Prop

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

		self.type = {0: 'integer'}
		for i in range(1, self.GetColumnCount()):
			self.type[i] = 'string'
		log.debug("prop.datamodel Initialization Complete")

	def GetColumnCount(self):
		# Report how many columns this model provides data for.
		log.trace("GetColumnCount")
		return 7

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
		log.trace("GetParent")
		return dv.NullDataViewItem

	def GetChildren(self, parent, children):
		# The view calls this method to find the children of any node in the
		# control. If the parent item is invalid then it represents the hidden root
		# item, so we'll use the genre objects as its children and they will
		# end up being the collection of visible roots in our tree.
		log.trace("GetChildren")
		if self.data and not parent:
			for item in self.data:
				children.append(self.ObjectToItem(item))
			return len(self.data)
		return 0

	def GetValue(self, item, col):
		# Return the value to be displayed for this item and column.
		log.trace("GetValue")

		node = self.ItemToObject(item)
		if isinstance(node, Prop):
			if node.PixelsAllocated:
				allocated = str(node.PixelsAllocated)
			else:
				allocated = str(node.Strings * node.Pixels)
			mapper = {0: str(node.ID),
					  1: node.Name,
					  2: str(node.Unit),
					  3: str(node.Strings),
					  4: str(node.Pixels),
					  5: allocated,
					  6: "{} {} {}".format(node.product.Style,
					                       node.product.Protocol,
			                               node.product.Details)
			          }
			return mapper[col]
		else:
			raise RuntimeError("unknown node type")

	def SetValue(self, value, item, col):
		# We're not allowing edits in column zero
		log.trace("SetValue: %s" % value)

		node = self.ItemToObject(item)
		if isinstance(node, Prop):
			self.session.begin(subtransactions=True)
			if col == 1:
				node.Name = value
			elif col == 2:
				node.Unit = value
			elif col == 3:
				node.Strings = value
				if node.Strings * node.Pixels == value:
					node.PixelsAllocated = None
			elif col == 4:
				node.Pixels = value
				if node.Strings * node.Pixels == value:
					node.PixelsAllocated = None
			elif col == 5:
				value = int(value)
				if value == 0 or node.Strings * node.Pixels == value:
					value = None
				node.PixelsAllocated = value
			self.session.commit()

	def addItem(self, items):
		self.session.begin(subtransactions=True)
		for item in items:
			new_prop = Prop(**item)
			self.session.add(new_prop)
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
	q = session.query(Prop).all()

	mdl = dataModel(q, session)
	print mdl
