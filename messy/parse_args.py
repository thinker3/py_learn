#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--count', type=int, help='count', default=1)  # default is None if not specified
parser.add_argument('-d', '--debug', action='store_true', help='debug')
parser.add_argument('-x', '--xxx', help='debug')
args = parser.parse_args()
print args.count
print args.debug
print args.xxx
