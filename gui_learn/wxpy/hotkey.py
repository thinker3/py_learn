#!/usr/bin/env python
# encoding: utf-8

import wx
import win32con


class FrameWithHotKey(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.regHotKey()
        self.Bind(wx.EVT_HOTKEY, self.handleHotKey, id=self.hotKeyId)
        self.Show()

    def regHotKey(self):
        # left alt + z
        self.hotKeyId = 100
        self.RegisterHotKey(
            self.hotKeyId,
            #0xA4,  # left alt, not works
            win32con.MOD_ALT,
            #0x5A,  # Z
            ord('Z'),
            )
    def handleHotKey(self, evt):
        print "do hot key actions"

app = wx.App()
FrameWithHotKey(None)
app.MainLoop()
