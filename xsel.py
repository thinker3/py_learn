#!/usr/bin/env python
# encoding: utf-8

import os


print os.popen('xsel').read().strip()
os.popen('xsel -c')
print os.popen('xsel').read().strip()
# how to set value?
