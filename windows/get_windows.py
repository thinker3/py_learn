#!/usr/bin/env python
# encoding: utf-8

import win32gui
import time


def windowEnumerationHandler(hwnd, resultList):
    resultList.append((hwnd, win32gui.GetWindowText(hwnd)))


def bringToFront(windowText):
    secondsPassed = 0
    while secondsPassed <= 5:
        time.sleep(1)

        topWindows = []
        win32gui.EnumWindows(windowEnumerationHandler, topWindows)
        print(len(topWindows))
        for i in topWindows:
            if windowText in i[1]:
                print(i)
                win32gui.ShowWindow(i[0], 5)
                win32gui.SetForegroundWindow(i[0])
        handle = win32gui.GetForegroundWindow()
        if windowText in win32gui.GetWindowText(handle):
            break
        else:
            secondsPassed += 1

bringToFront('wxpython')

import SendKeys
SendKeys.SendKeys('^a')
print('here')

'''
topWindows = []
win32gui.EnumWindows(windowEnumerationHandler, topWindows)
for id, text in topWindows:
    if text and not text in ['Default IME', 'MSCTFIME UI']:
        print id, text
handle = win32gui.GetForegroundWindow()
print handle
'''
