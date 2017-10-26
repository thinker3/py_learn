#!/usr/bin/env python
# -*- coding: utf-8 -*-

import errno

for k, v in errno.errorcode.iteritems():
    print k, v
