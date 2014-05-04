import os
import sys
import ctypes
from ctypes import wintypes
import win32con

byref = ctypes.byref
user32 = ctypes.windll.user32

id = 1
#if not user32.RegisterHotKey(None, id, win32con.MOD_WIN, win32con.VK_SHIFT):
r = user32.RegisterHotKey(None, id, win32con.MOD_CONTROL, win32con.VK_F1)
print r
if not r:
    print "Unable to register id", id

id += 1
r = user32.RegisterHotKey(None, id, win32con.MOD_CONTROL | win32con.MOD_ALT, 0x07)
print r
if not r:
    print "Unable to register id", id

msg = wintypes.MSG()
while user32.GetMessageA(byref(msg), None, 0, 0) != 0:
    print msg, msg.message
    if msg.message == win32con.WM_HOTKEY:
        print 'hello'

user32.TranslateMessage(byref(msg))
user32.DispatchMessageA(byref(msg))
