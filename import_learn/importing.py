#!/usr/bin/env python
# -*- coding: utf-8 -*-

# disable implicit relative importing
# even no jedi auto completion

#from date_format import
from __future__ import absolute_import

# ValueError: Attempted relative import in non-package
#from .imported import s

from messy.imported import s
print s

print '__file__ of importing is %s' % __file__
print '__name__ of importing is %s' % __name__

from messy.imported import decorated_func_import_test

decorated_func_import_test._original()
decorated_func_import_test()
