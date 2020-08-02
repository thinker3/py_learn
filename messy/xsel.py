#!/usr/bin/env python
# encoding: utf-8

import os


print(os.popen('xsel').read().strip())
os.popen('xsel -c')
print(os.popen('xsel').read().strip())
# how to set value?
os.popen('echo hello | xclip')
print(os.popen('xsel').read().strip())
os.popen('xsel -c')
