#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt

now = dt.datetime.now()
time = now.time()
print time.strftime('%H:%M')
print time.strftime('%H:%M:%S')
