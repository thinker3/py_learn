#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import ctypes.util

import objc
import CoreFoundation

Carbon = ctypes.util.find_library('Carbon')
carbon = ctypes.cdll.LoadLibrary(Carbon)
_objc = ctypes.PyDLL(objc._objc.__file__)

# PyObject *PyObjCObject_New(id objc_object, int flags, int retain)
_objc.PyObjCObject_New.restype = ctypes.py_object
_objc.PyObjCObject_New.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]

def objc_object(id):
    return _objc.PyObjCObject_New(id, 0, 1)

carbon.TISSelectInputSource.restype = ctypes.c_void_p
carbon.TISSelectInputSource.argtypes = [ctypes.c_void_p]

carbon.TISCopyInputSourceForLanguage.argtypes = [ctypes.c_void_p]
carbon.TISCopyInputSourceForLanguage.restype = ctypes.c_void_p

en = CoreFoundation.CFSTR(u'en').__c_void_p__()
en = carbon.TISCopyInputSourceForLanguage(en)
print en
#carbon.TISSelectInputSource(en)
