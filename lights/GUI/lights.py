# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.dataview

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lights: Configuration Tracker", pos = wx.DefaultPosition, size = wx.Size( 800,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.m_mgr = wx.aui.AuiManager()
		self.m_mgr.SetManagedWindow( self )
		self.m_mgr.SetFlags(wx.aui.AUI_MGR_ALLOW_ACTIVE_PANE|wx.aui.AUI_MGR_ALLOW_FLOATING|wx.aui.AUI_MGR_DEFAULT|wx.aui.AUI_MGR_LIVE_RESIZE)
		
		self.m_menubar4 = wx.MenuBar( 0 )
		self.SetMenuBar( self.m_menubar4 )
		
		self.m_statusBar4 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.m_mgr.Update()
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		self.m_mgr.UnInit()
		
	

###########################################################################
## Class treeFrame
###########################################################################

class treeFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lights: ", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		tree_bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.dataViewTreeCtrl = wx.dataview.DataViewTreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.HSCROLL|wx.TAB_TRAVERSAL|wx.VSCROLL )
		tree_bSizer.Add( self.dataViewTreeCtrl, 1, wx.ALL, 5 )
		
		
		self.SetSizer( tree_bSizer )
		self.Layout()
		self.tree_menubar = wx.MenuBar( 0 )
		self.file_wxMenu = wx.Menu()
		self.exit_menuitem = wx.MenuItem( self.file_wxMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_wxMenu.AppendItem( self.exit_menuitem )
		
		self.tree_menubar.Append( self.file_wxMenu, u"File" ) 
		
		self.db_wxMenu = wx.Menu()
		self.add_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Add", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.add_menuitem )
		
		self.del_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.del_menuitem )
		
		self.save_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.save_menuitem )
		
		self.refresh_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Refresh", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.refresh_menuitem )
		
		self.tree_menubar.Append( self.db_wxMenu, u"DB" ) 
		
		self.SetMenuBar( self.tree_menubar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.propExit, id = self.exit_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.addItem, id = self.add_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.delItem, id = self.del_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.saveRecs, id = self.save_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.refreshDB, id = self.refresh_menuitem.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def propExit( self, event ):
		event.Skip()
	
	def addItem( self, event ):
		event.Skip()
	
	def delItem( self, event ):
		event.Skip()
	
	def saveRecs( self, event ):
		event.Skip()
	
	def refreshDB( self, event ):
		event.Skip()
	

###########################################################################
## Class subFrame
###########################################################################

class subFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lights: Controllers", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.dataViewCtrl = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_SINGLE|wx.dataview.DV_VERT_RULES|wx.HSCROLL|wx.VSCROLL )
		self.dataViewCtrl.SetMinSize( wx.Size( 600,600 ) )
		
		bSizer.Add( self.dataViewCtrl, 1, wx.ALL, 5 )
		
		self.infoCtrl = wx.InfoBar( self )
		self.infoCtrl.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.infoCtrl.SetEffectDuration( 500 )
		bSizer.Add( self.infoCtrl, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		self.menubar = wx.MenuBar( 0 )
		self.file_wxMenu = wx.Menu()
		self.exit_menuitem = wx.MenuItem( self.file_wxMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_wxMenu.AppendItem( self.exit_menuitem )
		
		self.menubar.Append( self.file_wxMenu, u"File" ) 
		
		self.db_wxMenu = wx.Menu()
		self.add_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Add", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.add_menuitem )
		
		self.del_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.del_menuitem )
		
		self.save_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.save_menuitem )
		
		self.refresh_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Refresh", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.refresh_menuitem )
		
		self.menubar.Append( self.db_wxMenu, u"DB" ) 
		
		self.SetMenuBar( self.menubar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.fileExit, id = self.exit_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.addItem, id = self.add_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.delItem, id = self.del_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.saveRecs, id = self.save_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.refreshDB, id = self.refresh_menuitem.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def fileExit( self, event ):
		event.Skip()
	
	def addItem( self, event ):
		event.Skip()
	
	def delItem( self, event ):
		event.Skip()
	
	def saveRecs( self, event ):
		event.Skip()
	
	def refreshDB( self, event ):
		event.Skip()
	

