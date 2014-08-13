#!/usr/bin/env python
# encoding: utf-8

import gevent
from gevent.queue import Queue

tasks = Queue()


def worker(name):
    while not tasks.empty():
        task = tasks.get()
        print('Worker %s got task %s' % (name, task))
        # SystemError: (libev) select: Unknown error
        #gevent.sleep(1)
        gevent.sleep(0)

    print('Quitting time!')


def boss():
    for i in xrange(1, 25):
        print "Put in task %d" % i
        # SystemError: (libev) select: Unknown error
        #gevent.sleep(1)
        tasks.put_nowait(i)

gevent.spawn(boss).join()

gevent.joinall([
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'nancy'),
])
