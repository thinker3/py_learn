import os
import sys
import ctypes
from ctypes import wintypes
import win32con

byref = ctypes.byref
user32 = ctypes.windll.user32

id = 1
#if not user32.RegisterHotKey (None, id, win32con.MOD_WIN, win32con.VK_SHIFT):
if not user32.RegisterHotKey (None, id, win32con.MOD_CONTROL, win32con.VK_F1):
    print "Unable to register id", id

msg = wintypes.MSG ()
while user32.GetMessageA (byref (msg), None, 0, 0) != 0:
    if msg.message == win32con.WM_HOTKEY:
        print 'hello'
user32.TranslateMessage (byref (msg))
user32.DispatchMessageA (byref (msg))
