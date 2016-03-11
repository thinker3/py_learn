#!/usr/bin/env python
# encoding: utf-8

import wx
import time
import win32con
import win32com.client
import win32clipboard


def get_selected_text():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text


def get_original_text():
    try:
        win32clipboard.OpenClipboard()
        original_text = win32clipboard.GetClipboardData()
    except TypeError as e:
        original_text = ''
    finally:
        win32clipboard.CloseClipboard()
    return original_text


def reset_clipboard(original_text):
    temp = get_original_text()
    win32clipboard.OpenClipboard()
    if temp is not None:
        win32clipboard.EmptyClipboard()
    if original_text is not None:
        win32clipboard.SetClipboardText(original_text)
    win32clipboard.CloseClipboard()



class FrameWithHotKey(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.shell = win32com.client.Dispatch("WScript.Shell")
        self.regHotKey(1, win32con.MOD_ALT, 'z')
        self.regHotKey(2, win32con.MOD_WIN, 'z')
        self.regHotKey(3, win32con.MOD_SHIFT, 'z')
        self.Show()

    def send_keys(self, keys):
        self.shell.SendKeys(keys)

    def send_ctrl_c(self):
        self.send_keys("^c")

    def regHotKey(self, hotKeyId, mod, key):
        # left alt + z
        self.RegisterHotKey(
            hotKeyId,
            mod,
            ord(key.upper()),
            )
        self.Bind(wx.EVT_HOTKEY, self.handleHotKey, id=hotKeyId)

    def handleHotKey(self, evt):
        time.sleep(0.5)  # at least 0.3
        self.send_ctrl_c()
        time.sleep(0.1)
        print get_selected_text()

app = wx.App()
FrameWithHotKey(None)
app.MainLoop()
