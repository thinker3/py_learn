#!/usr/bin/env python
# encoding: utf-8


import os
import traceback


home = os.path.expanduser('~')
filename = 'not_exists.txt'
filepath = os.path.join(home, filename)
try:
    os.remove(filepath)
except Exception as e:
    print('*' * 100)
    print(e)
    print(type(e))
    print(type(e).__name__)
    print('*' * 100)
    traceback.print_exc()
    print('*' * 100)


filename = 'opened.txt'
filepath = os.path.join(home, filename)
f = open(filepath, 'w')
f.write('opened but not closed')
try:
    os.remove(filepath)
except WindowsError as e:
    print('*' * 100)
    print(e)
    print(type(e))
    print(type(e).__name__)
    print('*' * 100)
    traceback.print_exc()
    print('*' * 100)
    f.close()
    os.remove(filepath)


try:
    abc
except Exception as e:
    print('*' * 100)
    print(e)
    print(type(e))
    print(type(e).__name__)
    print('*' * 100)
    traceback.print_exc()
    print('*' * 100)
