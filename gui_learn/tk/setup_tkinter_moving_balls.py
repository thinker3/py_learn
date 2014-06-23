#!/usr/bin/env python
# encoding: utf-8

# python setup*.py py2exe

from distutils.core import setup
import py2exe

setup(
    windows = ['tkinter_moving_balls.py'],
)
