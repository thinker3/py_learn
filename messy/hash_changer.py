#!/usr/bin/env python
# encoding: utf-8

import os
import sys

pth = sys.argv[1]
pth = os.path.abspath(pth)

files = list(os.walk(pth))[0][2]
#print files
for f in files:
    f = os.path.join(pth, f)
    print f
    f = open(f, 'ab')
    f.write('0')
    f.close()
