#!/usr/bin/env python
# encoding: utf-8

import _winreg as wreg


def get_registry_value(key, subkey, value_name):
    key = getattr(wreg, key)
    '''
    _winreg.OpenKey(key, sub_key[, res[, sam]])
        res is a reserved integer, and must be zero. The default is zero.
        sam, Default is KEY_READ.
    _winreg.OpenKeyEx()
        The functionality of OpenKeyEx() is provided via OpenKey(), by the use of default arguments.
    '''
    handle = wreg.OpenKey(key, subkey)
    value = wreg.QueryValueEx(handle, value_name)
    print value


def set_registry_value(key, subkey, value_name, typ, value):
    key = getattr(wreg, key)
    #handle = wreg.OpenKey(key, subkey)
    handle = wreg.OpenKey(key, subkey, 0, wreg.KEY_SET_VALUE)
    '''
    _winreg.SetValue(key, sub_key, type, value)
    _winreg.SetValueEx(key, value_name, reserved, type, value)
        reserved can be anything – zero is always passed to the API.
    '''
    wreg.SetValueEx(handle, value_name, 0, typ, value)


def create_registry_value(key, subkey, value_name, typ, value):
    key = getattr(wreg, key)
    handle = wreg.CreateKey(key, subkey)
    wreg.SetValueEx(handle, value_name, 0, typ, value)


def delete_registry_value(key, subkey, value_name):
    key = getattr(wreg, key)
    handle = wreg.OpenKey(key, subkey, 0, wreg.KEY_ALL_ACCESS)
    wreg.DeleteValue(handle, value_name)

#get_registry_value('HKEY_CURRENT_USER', 'Console\\Windows 命令处理程序', 'quickedit')
get_registry_value('HKEY_CURRENT_USER', 'Console\Windows 命令处理程序', 'quickedit')
create_registry_value('HKEY_CURRENT_USER', 'Console\Windows 命令处理程序', 'test', wreg.REG_SZ, 'test value')
raw_input('Press any key to continue...')
get_registry_value('HKEY_CURRENT_USER', 'Console\Windows 命令处理程序', 'test')
set_registry_value('HKEY_CURRENT_USER', 'Console\Windows 命令处理程序', 'test', wreg.REG_DWORD, 0x1000)
get_registry_value('HKEY_CURRENT_USER', 'Console\Windows 命令处理程序', 'test')
delete_registry_value('HKEY_CURRENT_USER', 'Console\Windows 命令处理程序', 'test')
