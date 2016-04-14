# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 650,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.main_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		bSizer5.Add( self.main_notebook, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer5 )
		self.Layout()
		self.main_menubar = wx.MenuBar( 0 )
		self.file_wxMenu = wx.Menu()
		self.exit_menuitem = wx.MenuItem( self.file_wxMenu, wx.ID_ANY, u"Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.file_wxMenu.AppendItem( self.exit_menuitem )
		
		self.main_menubar.Append( self.file_wxMenu, u"File" ) 
		
		self.edit_wxMenu = wx.Menu()
		self.add_menuitem = wx.MenuItem( self.edit_wxMenu, wx.ID_ANY, u"Add", wx.EmptyString, wx.ITEM_NORMAL )
		self.edit_wxMenu.AppendItem( self.add_menuitem )
		
		self.del_menuitem = wx.MenuItem( self.edit_wxMenu, wx.ID_ANY, u"Delete", wx.EmptyString, wx.ITEM_NORMAL )
		self.edit_wxMenu.AppendItem( self.del_menuitem )
		
		self.main_menubar.Append( self.edit_wxMenu, u"Edit" ) 
		
		self.SetMenuBar( self.main_menubar )
		
		self.main_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.flleExit, id = self.exit_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.addItem, id = self.add_menuitem.GetId() )
		self.Bind( wx.EVT_MENU, self.delItem, id = self.del_menuitem.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def flleExit( self, event ):
		event.Skip()
	
	def addItem( self, event ):
		event.Skip()
	
	def delItem( self, event ):
		event.Skip()
	

###########################################################################
## Class subPanel
###########################################################################

class subPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,800 ), style = wx.TAB_TRAVERSAL )
		
		bSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.toolbar = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TB_HORIZONTAL ) 
		self.add = self.toolbar.AddLabelTool( wx.ID_ANY, u"Add", wx.Bitmap( u"../icons/add_star-22.jpg", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.delete = self.toolbar.AddLabelTool( wx.ID_ANY, u"Delete", wx.Bitmap( u"../icons/delete.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.exit = self.toolbar.AddLabelTool( wx.ID_ANY, u"Exit", wx.Bitmap( u"../icons/exit-22.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.Realize() 
		
		bSizer.Add( self.toolbar, 0, wx.EXPAND, 5 )
		
		self.dataViewCtrl = wx.dataview.DataViewCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.DV_HORIZ_RULES|wx.dataview.DV_ROW_LINES|wx.dataview.DV_SINGLE|wx.dataview.DV_VERT_RULES|wx.HSCROLL|wx.VSCROLL )
		self.dataViewCtrl.SetMinSize( wx.Size( 600,600 ) )
		
		bSizer.Add( self.dataViewCtrl, 1, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer )
		self.Layout()
		
		# Connect Events
		self.Bind( wx.EVT_TOOL, self.addItem, id = self.add.GetId() )
		self.Bind( wx.EVT_TOOL, self.delItem, id = self.delete.GetId() )
		self.Bind( wx.EVT_TOOL, self.Exit, id = self.exit.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addItem( self, event ):
		event.Skip()
	
	def delItem( self, event ):
		event.Skip()
	
	def Exit( self, event ):
		event.Skip()
	

###########################################################################
## Class addProp
###########################################################################

class addProp ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lights: Add Prop", pos = wx.DefaultPosition, size = wx.Size( 645,291 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.name, 1, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Details" ), wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 6, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Strings", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.strings = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 999, 1 )
		fgSizer1.Add( self.strings, 1, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Pixels", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.pixels = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 9999, 1 )
		fgSizer1.Add( self.pixels, 0, wx.ALL, 5 )
		
		self.m_staticText17 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Allocated:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )
		fgSizer1.Add( self.m_staticText17, 0, wx.ALL, 5 )
		
		self.allocated = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 99999, 0 )
		fgSizer1.Add( self.allocated, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Units", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.units = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 9999, 1 )
		fgSizer1.Add( self.units, 1, wx.ALL, 5 )
		
		self.m_staticText15 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		fgSizer1.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.start_number = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 99999, 1 )
		fgSizer1.Add( self.start_number, 1, wx.ALL, 5 )
		
		
		sbSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Product Used" ), wx.HORIZONTAL )
		
		productChoices = []
		self.product = wx.ComboBox( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, productChoices, 0 )
		self.product.SetSelection( 0 )
		sbSizer4.Add( self.product, 1, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer4, 0, wx.EXPAND, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		
		bSizer3.Add( m_sdbSizer1, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.addProp )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addProp( self, event ):
		event.Skip()
	

###########################################################################
## Class addController
###########################################################################

class addController ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Lights: Add Controller", pos = wx.DefaultPosition, size = wx.Size( 645,291 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer5.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.name, 1, wx.ALL, 5 )
		
		
		bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Details" ), wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 4, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"IP Addr", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.ipaddr = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 254, 230 )
		fgSizer1.Add( self.ipaddr, 1, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Universe", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		fgSizer1.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		self.universe = wx.SpinCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 1, 9999, 1 )
		fgSizer1.Add( self.universe, 0, wx.ALL, 5 )
		
		
		sbSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		bSizer3.Add( sbSizer2, 0, wx.EXPAND, 5 )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Model" ), wx.HORIZONTAL )
		
		modelChoices = []
		self.model = wx.ComboBox( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, modelChoices, 0 )
		self.model.SetSelection( 0 )
		sbSizer4.Add( self.model, 1, wx.ALL, 5 )
		
		
		bSizer3.Add( sbSizer4, 0, wx.EXPAND, 5 )
		
		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		self.m_sdbSizer1Cancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer1.AddButton( self.m_sdbSizer1Cancel )
		m_sdbSizer1.Realize();
		
		bSizer3.Add( m_sdbSizer1, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_sdbSizer1OK.Bind( wx.EVT_BUTTON, self.addItem )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def addItem( self, event ):
		event.Skip()
	

