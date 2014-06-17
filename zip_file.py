#!/usr/bin/env python
# encoding: utf-8

import os
import zipfile

dirname = os.path.dirname(os.path.abspath(__file__))
basename = 'class_static_method.py'
fullname = os.path.join(dirname, basename)
output = os.path.join(dirname, 'test.zip')

dst = zipfile.ZipFile(output, 'w')
dst.write(fullname, basename)
dst.close()
