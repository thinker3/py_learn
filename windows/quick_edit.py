#!/usr/bin/env python
# encoding: utf-8

import time
import random
import ctypes


win32 = ctypes.windll.kernel32
hin = win32.GetStdHandle(-10)
mode = ctypes.c_int(0)
win32.GetConsoleMode(hin, ctypes.byref(mode))
old_mode = mode.value
# disable Windows console(cmd.exe) quick edit mode
new_mode = old_mode & (~0x0040)
win32.SetConsoleMode(hin, new_mode)

running = True
while running:
    try:
        r = random.randint(1, 7)
        print('hello %s' % r)
        if r == 4:
            1/0
        time.sleep(1)
    except (Exception, KeyboardInterrupt):
        win32.SetConsoleMode(hin, old_mode)
        running = False
