#!/usr/bin/env python
# encoding: utf-8


def coroutine(func):
    def start(*args, **kwargs):
        g = func(*args, **kwargs)
        g.next()
        return g
    return start


@coroutine
def printer():
    while True:
        msg = yield
        print 'printing %s' % msg


@coroutine
def logger():
    while True:
        msg = yield
        print 'logging %s' % msg


targets = [printer(), logger()]
for t in targets:
    t.send('hello')
    t.send('world')
    t.close()
