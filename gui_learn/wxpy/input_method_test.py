#!/usr/bin/env python
# encoding: utf-8

import wx


class InputMethodTest(wx.Frame):
    height = 200
    width = 500
    size = (width, height)

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=self.size)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)
        self.Center()

app = wx.App(False)
frame = InputMethodTest(None, 'Can you input Chinese?')
app.MainLoop()
