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
## Class propFrame
###########################################################################

class propFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lights: Props", pos = wx.DefaultPosition, size = wx.Size( 600,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		prop_bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.prop_dataViewCtrl = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_SINGLE|wx.dataview.DV_VERT_RULES|wx.HSCROLL|wx.VSCROLL )
		self.prop_dataViewCtrl.SetMinSize( wx.Size( 600,600 ) )
		
		prop_bSizer.Add( self.prop_dataViewCtrl, 0, wx.ALL, 5 )
		
		self.prop_infoCtrl = wx.InfoBar( self )
		self.prop_infoCtrl.SetShowHideEffects( wx.SHOW_EFFECT_NONE, wx.SHOW_EFFECT_NONE )
		self.prop_infoCtrl.SetEffectDuration( 500 )
		prop_bSizer.Add( self.prop_infoCtrl, 0, wx.ALL, 5 )
		
		
		self.SetSizer( prop_bSizer )
		self.Layout()
		self.prop_menubar = wx.MenuBar( 0 )
		self.file_wxMenu = wx.Menu()
		self.prop_exit_menuitem = wx.MenuItem( self.file_wxMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_wxMenu.AppendItem( self.prop_exit_menuitem )
		
		self.prop_menubar.Append( self.file_wxMenu, u"File" ) 
		
		self.db_wxMenu = wx.Menu()
		self.prop_add_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Add", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.prop_add_menuitem )
		
		self.prop_del_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.prop_del_menuitem )
		
		self.prop_save_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.prop_save_menuitem )
		
		self.prop_refresh_menuitem = wx.MenuItem( self.db_wxMenu, wx.ID_ANY, u"Refresh", wx.EmptyString, wx.ITEM_NORMAL )
		self.db_wxMenu.AppendItem( self.prop_refresh_menuitem )
		
		self.prop_menubar.Append( self.db_wxMenu, u"DB" ) 
		
		self.SetMenuBar( self.prop_menubar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.propExit, id = self.prop_exit_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.addProp, id = self.prop_add_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.delProp, id = self.prop_del_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.saveProp, id = self.prop_save_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.refreshProp, id = self.prop_refresh_menuitem.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def propExit( self, event ):
		event.Skip()
	
	def addProp( self, event ):
		event.Skip()
	
	def delProp( self, event ):
		event.Skip()
	
	def saveProp( self, event ):
		event.Skip()
	
	def refreshProp( self, event ):
		event.Skip()
	

