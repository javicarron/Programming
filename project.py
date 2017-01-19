#!/usr/bin/env python
import wx
import os
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()
        
        filemenu=wx.Menu()
        menuOpen= filemenu.Append(wx.ID_OPEN, "&Open", "Open text file")
        filemenu.AppendSeparator()
        menuExit= filemenu.Append(wx.ID_EXIT,"E&xit", "Terminate this program")
        
        helpmenu=wx.Menu()
        menuAbout= helpmenu.Append(wx.ID_ABOUT, "&About", "Information about this program")
        
        menuBar=wx.MenuBar()
        menuBar.Append(filemenu,"&File")
        menuBar.Append(helpmenu, "&Help")
        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnOpen, menuOpen)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        
        
        self.sizer2=wx.BoxSizer(wx.HORIZONTAL)
        Buttons= self.buttons =[]
        self.buttons.append(wx.Button(self, 0, "Open"))
        self.sizer2.Add(self.buttons[0], 1, wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.OnOpen, Buttons[0])
        for i in range(1,6):
            self.buttons.append(wx.Button(self, 0, "Button &"+str(i)))
            self.sizer2.Add(self.buttons[i], 1, wx.EXPAND)
            
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.sizer2, 0, wx.EXPAND)
        self.sizer.Add(self.control, 1, wx.EXPAND)
        
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        #self.sizer.Fit(self)     
        self.SetSize((500,400))
        
        self.Show(True)
        
    
    def OnAbout(self,e):
        dlg = wx.MessageDialog(self, "A small yet undefined project", "About this project", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()
        
    def OnExit(self,e):
        wx.ColourPickerCtrl()
        
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
        
        
app = wx.App(False)
frame = MainWindow(None, "Project")
app.MainLoop()