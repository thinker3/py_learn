#!/usr/bin/env python
# encoding: utf-8

import time
import datetime

d = {
    'now': datetime.datetime.now(),
}

print d['now']
time.sleep(0.5)
print d['now']


d = {
    'now': lambda: datetime.datetime.now(),
}

print d['now']()
time.sleep(0.5)
print d['now']()
