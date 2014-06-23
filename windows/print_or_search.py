#!/usr/bin/env python
#coding: utf8

import sys
import pyhk
import win32gui
import win32clipboard
import SendKeys
from youdao import query_web
 
def exit():
    sys.exit()

def get_selected_text():
    handle = win32gui.GetForegroundWindow()
    title =  win32gui.GetWindowText(handle)
    if 'cmd.exe' in title or u'命令处理程序' in title.decode('gbk') or (
            title.startswith('python') and title.strip().endswith('.py')):
        return None
    else:
        SendKeys.SendKeys('^c')
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text

def get_original_text():
    win32clipboard.OpenClipboard()
    try:
        original_text = win32clipboard.GetClipboardData()
    except TypeError as e:
        original_text = None
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


def search():
    original_text = get_original_text()
    print 'original_text: %s' % original_text
    selected_text = get_selected_text()
    print 'selected text: %s' % selected_text
    reset_clipboard(original_text)
    if selected_text:
        query_web(selected_text)
    else:
        print 'wrong word?'


def print_selection():
    original_text = get_original_text()
    print 'original_text: %s' % original_text
    selected_text = get_selected_text()
    print 'selected text: %s' % selected_text
    reset_clipboard(original_text)
    print


def get_selection():
    original_text = get_original_text()
    selected_text = get_selected_text()
    reset_clipboard(original_text)
    return selected_text

hot = pyhk.pyhk()

if __name__ == '__main__':
    # ctrl + shift + q to quit
    #hot.addHotkey(['Ctrl', 'Lwin', '1'], search)
    hot.addHotkey(['Ctrl', 'Lwin', '1'], print_selection)  # c-Lwin or c-1 works

    # letters must be upper
    # pyhk is problematic
    #hot.addHotkey(['Lwin', 'Z'], print_selection)
    #hot.addHotkey(['Ctrl', 'Lwin'], print_selection)
    #hot.addHotkey(['Ctrl', 'Alt', 'Z'], print_selection)
    #hot.addHotkey(['Ctrl', 'Alt', 'Z'], search)
    hot.start()
