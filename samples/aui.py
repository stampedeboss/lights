import wx
import wx.dataview
import wx.lib.agw.aui as aui
import wx.dataview as dv

from sqlalchemy.orm import create_session

from lights import Lights, Prop
from lights.prop.datamodel import dataModel


class MyFrame(wx.Frame):

	def __init__(self, parent, id=-1, title="AUI Test", pos=wx.DefaultPosition,
				 size=(800, 600), style=wx.DEFAULT_FRAME_STYLE):

		wx.Frame.__init__(self, parent, id, title, pos, size, style)

		self._mgr = aui.AuiManager()

		# notify AUI which frame to use
		self._mgr.SetManagedWindow(self)

		# create several text controls
		text1 = wx.TextCtrl(self, -1, "Prop",
							wx.DefaultPosition, wx.Size(200,150),
							wx.NO_BORDER | wx.TE_MULTILINE)

		text2 = wx.TextCtrl(self, -1, "Pane 2 - sample text",
							wx.DefaultPosition, wx.Size(200,150),
							wx.NO_BORDER | wx.TE_MULTILINE)

		text3 = wx.TextCtrl(self, -1, "Main content window",
							wx.DefaultPosition, wx.Size(200,150),
							wx.NO_BORDER | wx.TE_MULTILINE)

		data1 = wx.dataview.DataViewCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
				wx.dataview.DV_HORIZ_RULES | wx.dataview.DV_ROW_LINES | wx.dataview.DV_SINGLE | wx.dataview.DV_VERT_RULES)

		# Create a session to use the tables
		session = create_session(bind=Lights.engine)
		props = session.query(Prop).all()

		self.mdl = dataModel(props)

		data1.AssociateModel(self.mdl)
		# Define the columns that we want in the view.  Notice the
		# parameter which tells the view which col in the data model to pull
		# values from for each view column.
		if 0:
			self.tr = tr = dv.DataViewTextRenderer()
			c0 = dv.DataViewColumn("ID",  # title
								   tr,  # renderer
								   0,  # data model column
								   width=80)
			data1.AppendColumn(c0)
		else:
			data1.AppendTextColumn("Name", 1, width=150)

		c1 = data1.AppendTextColumn("Unit", 2, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c2 = data1.AppendTextColumn("Strings", 3, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c3 = data1.AppendTextColumn('Pixels', 4, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c4 = data1.AppendTextColumn('Allocated', 5, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)
		c5 = data1.AppendTextColumn('Item', 6, width=75, mode=dv.DATAVIEW_CELL_EDITABLE)

		c1.Alignment = wx.ALIGN_RIGHT
		c2.Alignment = wx.ALIGN_RIGHT
		c3.Alignment = wx.ALIGN_RIGHT
		c4.Alignment = wx.ALIGN_RIGHT
		c5.Alignment = wx.ALIGN_RIGHT

		# Set some additional attributes for all the columns
		for c in data1.Columns:
			c.Sortable = True
			c.Reorderable = True

		# add the panes to the manager
		self._mgr.AddPane(data1, aui.AuiPaneInfo().Left().Caption("Pane Number One"))
		self._mgr.AddPane(text2, aui.AuiPaneInfo().Bottom().Caption("Pane Number Two"))
		self._mgr.AddPane(text3, aui.AuiPaneInfo().CenterPane())

		# tell the manager to "commit" all the changes just made
		self._mgr.Update()

		self.Bind(wx.EVT_CLOSE, self.OnClose)


	def OnClose(self, event):

		# deinitialize the frame manager
		self._mgr.UnInit()

		self.Destroy()
		event.Skip()


# our normal wxApp-derived class, as usual

app = wx.App(0)

frame = MyFrame(None)
app.SetTopWindow(frame)
frame.Show()

app.MainLoop()
