#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	----------------------------------------------------------------------
	This model acts as a bridge between the DataViewCtrl and the data

	This model provides these data columns:
		 0.  DisplayName:   string
		 1.  ControllerName:string
		 2.  Connector:     integer
		 3.  TotalChannels: integer
		 4.  TotalPixels:   integer
		 5.  UniverseStart: integer
		 6.  UniverseEnd:   integer
		 7.  ChannelStart:  integer
		 8.  ChannelEnd:    integer
		 9. xLightStart:   integer
		 10. xLightEnd:     integer
'''

import wx
import logging
import wx.dataview as dv

from lights import Session, Display, Connections, Prop, Controllers, Connectors

__pgmname__ = 'datamodel'

__author__ = "AJ Reynolds"
__email__ = "stampedeboss@gmail.com"

__maintainer__ = __author__

__copyright__ = "Copyright 2016, AJ Reynolds"
__license__ = "CC0"

log = logging.getLogger(__pgmname__)


class dataModel(dv.PyDataViewModel):

	def __init__(self, data, session):
		log.trace("__init__")
		super(dataModel, self).__init__()
		self.data = data
		self.session = session
		self.objmapper.UseWeakRefs(True)

		self.type = {0: 'string'}
		for i in range(1, self.GetColumnCount()):
			self.type[i] = 'string'

		self.tracking ={}
		log.debug("connection.datamodel Initialization Complete")

	def GetColumnCount(self):
		# Report how many columns this model provides data for.
		log.trace("GetColumnCount")
		return 11

	def GetColumnType(self, col):
		# Map the data column numbers to the data type
		log.trace("GetColumnType")
		return self.type[col]

	def IsContainer(self, item):
		# Return True if the item has children, False otherwise.
		# The hidden root is a container
		log.trace("IsContainer: {}".format(item))
		if not item:
			return True
		# and in this model the genre objects are containers
		# node = self.ItemToObject(item)
		# if isinstance(node, Display):
		# 	return True
		# but everything else are not
		return False

	def GetParent(self, item):
		log.trace("GetParent: {}".format(item))
		if not item:
			return dv.NullDataViewItem
		return dv.NullDataViewItem

		node = self.ItemToObject(item)
		if isinstance(node, Display):
			return dv.NullDataViewItem
		# elif isinstance(node, Controllers):
		# 	for connector in node.connectors:
		# 		return self.ObjectToItem(connector.connection.display)
		# elif isinstance(node, Connections):
		# 	return self.ObjectToItem(node.connector.controller)

	def GetChildren(self, parent, children):
		log.trace("GetChildren")
		# The view calls this method to find the children of any node in the
		# control. There is an implicit hidden root node, and the top level
		# item(s) should be reported as children of this node. A List view
		# simply provides all items as children of this hidden root. A Tree
		# view adds additional items as children of the other items, as needed,
		# to provide the tree hierachy.

		# If the parent item is invalid then it represents the hidden root
		# item, so we'll use the genre objects as its children and they will
		# end up being the collection of visible roots in our tree.
		if not parent:
			for item in self.data:
				children.append(self.ObjectToItem(item))
			return len(children)

		# Otherwise we'll fetch the python object associated with the parent
		# item and make DV items for each of it's child objects.
		# node = self.ItemToObject(parent)
		# if isinstance(node, Display):
		# 	for item in self.data:
		# 		if item.connector and item.connector.controller:
		# 			children.append(self.ObjectToItem(item.connector.controller))
		# 	test = len(children)
		# 	return len(children)
		# if isinstance(node, Controllers):
		# 	for item in node.connectors:
		# 		if item.connection:
		# 			children.append(self.ObjectToItem(item.connection))
		# 	test = len(children)
		# 	return len(children)
		return 0

	def GetValue(self, item, col):
		# Return the value to be displayed for this item and column.
		log.trace("GetValue")
		mapper= {}
		for i in range(0, self.GetColumnCount()):
			mapper[i] = None

		node = self.ItemToObject(item)
		if isinstance(node, Display):
			mapper[0] = node.DisplayName
			return mapper[col]
		elif isinstance(node, Controllers):
			if not node.Name in self.tracking:
				self.tracking[node.Name] = {"nextUnivers": node.Universe, "nextChannel": 1 }
			mapper[1] = node.Name
			return mapper[col]
		elif isinstance(node, Connections):
			total_pixels = 0
			universe_start = 0
			universe_end = 0
			channel_start = 0
			channel_end = 0
			xlight_start = 0
			xlight_end = 0
			for entry in self.data:
				if node.DisplayID == entry.DisplayID \
					and node.ControllerID == entry.ControllerID \
					and node.Connector == entry.Connector:
						if entry.propIn.PixelsAllocated:
							allocated = entry.propIn.PixelsAllocated
						else:
							allocated = entry.propIn.Strings * entry.propIn.Pixels
						total_pixels += allocated
			mapper[0] = node.display.DisplayName
			if  node.Connector:
				mapper[2] = node.Connector
				if node.connector.controller:
					mapper[1] = node.connector.controller.Name
			mapper[3] = total_pixels
			mapper[4] = total_pixels * 3
			mapper[5] = universe_start
			mapper[6] = universe_end
			mapper[7] = channel_start
			mapper[8] = channel_end
			mapper[9] = xlight_start
			mapper[10] = xlight_end
			return str(mapper[col])
		else:
			raise RuntimeError("unknown node type")

	def SetValue(self, value, item, col):
		# We're not allowing edits in column zero
		log.trace("SetValue: %s" % value)

		node = self.ItemToObject(item)
		if isinstance(node, Controllers):
			self.session.begin(subtransactions=True)
			if col == 1:
				node.Name = value
			elif col == 2:
				node.IP_Address = value
			elif col == 3:
				node.Universe = value
			elif col == 4:
				node.Seq = value
			elif col == 5:
				node.CtlrModelID = value
			self.session.commit()

	def addItem(self, item):
		self.session.begin(subtransactions=True)
		self.session.add(item)
		self.session.commit()

	def delItem(self):
		# TODO: Implement delItem Prop
		pass

	def saveRecs(self):
		# TODO: Implement saveRecs Prop
		pass

	def refreshDB(self):
		# self.mdl.Cleared()
		self.Show()
		print


if __name__ == '__main__':
	from lights import Lights
	from sys import argv
	lights = Lights()
	lights.ParseArgs(argv[1:], test=True)

	app = wx.App(False)
	# Create a session to use the tables
	mdl = dataModel()
	print mdl