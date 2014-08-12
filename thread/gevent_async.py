#!/usr/bin/env python
# encoding: utf-8

# SystemError: (libev) select: Unknown error
import socket

import gevent
import random

def task(pid):
    gevent.sleep(random.randint(0, 9) * 0.1)
    print('Task %s done' % pid)

def synchronous():
    for i in range(1,10):
        task(i)

def asynchronous():
    threads = [gevent.spawn(task, i) for i in xrange(10)]
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
