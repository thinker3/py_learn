#!/usr/bin/env python
# encoding: utf-8

import ctypes
import ctypes.wintypes as wt
import win32con

user32 = ctypes.windll.user32


class GlobalHotKey(object):
    running = True
    key_mapping = []

    MOD_ALT = win32con.MOD_ALT
    MOD_CTRL = win32con.MOD_CONTROL
    MOD_CONTROL = win32con.MOD_CONTROL
    MOD_SHIFT = win32con.MOD_SHIFT
    MOD_WIN = win32con.MOD_WIN

    @classmethod
    def register(cls, vk, modifier=0, func=None):
        key_code = ord(vk.upper())
        if func is None:
            def register_decorator(f):
                cls.register(vk, modifier, f)
                return f
            return register_decorator
        else:
            cls.key_mapping.append((key_code, modifier, func))

    @classmethod
    def listen(cls):
        for index_id, (key_code, modifiers, func) in enumerate(cls.key_mapping):
            user32.RegisterHotKey(None, index_id, modifiers, key_code)
        try:
            msg = wt.MSG()
            while cls.running and user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                if msg.message == win32con.WM_HOTKEY:
                    (key_code, modifiers, func) = cls.key_mapping[msg.wParam]
                    if not func:
                        break
                    func()
                user32.TranslateMessage(ctypes.byref(msg))
                user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            for index_id, (key_code, modifiers, func) in enumerate(cls.key_mapping):
                user32.UnregisterHotKey(None, index_id)

def main():
    # press ctrl-c to quit
    GlobalHotKey.register('c', GlobalHotKey.MOD_CTRL, False)


    @GlobalHotKey.register('c', GlobalHotKey.MOD_ALT)
    def test():
        print 'hello'


    GlobalHotKey.listen()


if __name__ == '__main__':
    main()
