#!/usr/bin/env python
# encoding: utf-8

import sys 
import locale


def p(f):
    print('%s.%s(): %s' % (f.__module__, f.__name__, f()))

p(sys.getdefaultencoding)
p(sys.getfilesystemencoding)
p(locale.getdefaultlocale)
p(locale.getpreferredencoding)
