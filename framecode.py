#!/usr/bin/env python
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
        #Parent, ID, Title
frame.Show(True)
app.MainLoop()