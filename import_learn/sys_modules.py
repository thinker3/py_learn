#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes
import ctypes.util

# import sys
sys = ctypes._sys

for mod, v in sys.modules.iteritems():
    if any(sub in mod for sub in ['types', 'util']):
        print mod
        print "\t", v
