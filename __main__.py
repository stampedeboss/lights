"""
Purpose:


"""
import os
import logging
import wx
from sys import argv

from lights import Lights
from lights.GUI.lights import mainFrame as MF
from lights.prop.subpanel import subPanel as propPanel
from lights.controller.subpanel import subPanel as ctlrPanel
from lights.display.subpanel import subPanel as displayPanel

__pgmname__ = "lights"

log = logging.getLogger(__pgmname__)


def main(args=None):

	lights = Lights()
	lights.ParseArgs(argv[1:], test=True)

	app = wx.App(False)
	mf = mainFrame(None)
	prop_page = propPanel(mf.main_notebook, mf)
	ctlr_page = ctlrPanel(mf.main_notebook, mf)
	display_page = displayPanel(mf.main_notebook, mf)
	mf.main_notebook.AddPage(prop_page, "Props")
	mf.main_notebook.AddPage(ctlr_page, "Controllers")
	mf.main_notebook.AddPage(display_page, "Displays")
	mf.Show()
	app.MainLoop()


# Implementing mainFrame
class mainFrame( MF ):
	def __init__( self, parent ):
		super(mainFrame, self).__init__(parent)

	# Handlers for mainFrame events.
	def flleExit( self, event ):
		self.Close()

	def addItem( self, event ):
		# TODO: Implement addItem
		pass

	def delItem( self, event ):
		# TODO: Implement delItem
		pass


if __name__ == "__main__":
	main()
