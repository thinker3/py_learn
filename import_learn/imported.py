#!/usr/bin/env python
# -*- coding: utf-8 -*-

from utils.decorators import decorate

s = 'hello'
print '__file__ of imported is %s' % __file__
print '__name__ of imported is %s' % __name__


@decorate
def decorated_func_import_test():
    print 'decorated_func_import_test'
