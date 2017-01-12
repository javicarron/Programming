#!/usr/bin/env python
import wx
import os
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,800))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        
        filemenu=wx.Menu()
        menuAbout= filemenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        menuJoke= filemenu.Append(wx.ID_ANY, "Joke", "Want a joke?")
        menuOpen= filemenu.Append(wx.ID_OPEN, "&Open", "Open text file")
        filemenu.AppendSeparator()
        menuExit= filemenu.Append(wx.ID_EXIT,"E&xit", "Terminate this program")
        
        menuBar=wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnJoke, menuJoke)
        
        self.sizer2=wx.BoxSizer(wx.HORIZONTAL)
        self.buttons =[]
        for i in range(0,6):
            self.buttons.append(wx.Button(self, -1, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)
            
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)
        
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)     
        
        self.Show(True)
        
    
    def OnAbout(self,e):
        dlg = wx.MessageDialog(self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnExit(self,e):
        self.Close(True)
        
    def OnOpen(self,e):
        self.dirname=''
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy
        
    def OnJoke(self,e):
        dlg = wx.MessageDialog(self, "-How much does your Python directory weight? -Oh, it weights Pi-tons","A bad joke",  wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
        
app = wx.App(False)
frame = MainWindow(None, "Sample editor")
app.MainLoop()