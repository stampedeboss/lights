#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
	----------------------------------------------------------------------
	This model acts as a bridge between the DataViewCtrl and the Controller data, and
	organizes it hierarchically as a collection of Prop.

	This model provides these data columns:

		 0. ID:      integer
		 1. Name:    string
		 2. IP_Address: string
		 3. Universe: integer
		 4. Seq:  integer
		 5. CtlrModelID: Integer
		 6: Mfg: String
		 7: Model: String
		 8: Outputs: Integer
'''

import wx
import logging
import wx.dataview as dv

from lights import Controllers

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
		log.debug("controller.datamodel Initialization Complete")

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
		log.trace("GetParent")
		return dv.NullDataViewItem

	def GetChildren(self, parent, children):
		# The view calls this method to find the children of any node in the
		# control. If the parent item is invalid then it represents the hidden root
		# item, so we'll use the genre objects as its children and they will
		# end up being the collection of visible roots in our tree.
		log.trace("GetChildren")
		if not parent:
			for item in self.data:
				children.append(self.ObjectToItem(item))
			return len(self.data)
		return 0

	def GetValue(self, item, col):
		# Return the value to be displayed for this item and column.
		log.trace("GetValue")

		node = self.ItemToObject(item)
		if isinstance(node, Controllers):
			mapper = {0: str(node.ID),
					  1: node.Name,
					  2: str(node.IP_Address),
					  3: str(node.Universe),
					  4: str(node.Seq),
					  5: str(node.CtlrModelID),
			          6: str(node.model.Mfg),
					  7: str(node.model.Model),
					  8: str(node.model.Outputs)
			          }
			return mapper[col]
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

	from lights import Session

	app = wx.App(False)
	# Create a session to use the tables
	session = Session()
	db = session.query(Controllers).all()

	mdl = dataModel(db, session)
	print mdl