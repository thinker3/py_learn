#!/usr/bin/env python
# encoding: utf-8

import cgi


form = cgi.FieldStorage()
for one in dir(form):
    print(one)
print(form)
