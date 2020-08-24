#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('-h', '--host', default="localhost")  # -h, --help is reserved
parser.add_argument('-c', '--count', type=int, help='count', default=1)  # default is None if not specified
parser.add_argument('-d', '--debug', action='store_true', help='debug or not')
parser.add_argument('-u', '--username', help='username to login', default='admin')
args = parser.parse_args()
print(args.count)
print(args.debug)
print(args.username)
