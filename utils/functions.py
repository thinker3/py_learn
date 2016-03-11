#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def divide(sep='*', length=30):
    print sep * length


def abs_path(root, filename):
    dirname = os.path.dirname(os.path.abspath(root))
    return os.path.join(dirname, filename)
