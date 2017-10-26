#!/usr/bin/env python
# encoding: utf-8

from datetime import (
    datetime,
)


def decorate(func):
    print 'decorate is called'

    def _func(*args, **kwargs):
        print '_func is called'
        return func(*args, **kwargs)
    _func._original = func
    return _func


def segregate(func):
    # @segregate, without ()
    def _func(*args, **kwargs):
        print func.__name__
        func(*args, **kwargs)
        print '*' * 30
    return _func


def separate(sep='*', length=30):
    # @separate, with ()
    def _wrapper(func):
        def _func(*args, **kwargs):
            print func.__name__
            func(*args, **kwargs)
            print sep * length
        return _func
    return _wrapper


def smart_separate(*arg, **kwargs):
    def separate(sep='-', length=50):
        def wrapper(func):
            def _func(*args, **kwargs):
                r = func(*args, **kwargs)
                print sep * length
                return r
            return _func
        return wrapper

    if args:
        first = args[0]
        if type(first) == 'function':
            return wrapper(first)


def isolate(*args, **kwargs):
    # @isolate, with or without ()
    if len(args) == 1 and callable(args[0]):
        return segregate(args[0])
    sep = kwargs.get('sep') or '*'
    length = kwargs.get('length') or 30
    return separate(sep, length)


def show_time_interval(func):
    def _func(*args, **kwargs):
        before = datetime.now()
        ans = func(*args, **kwargs)
        delta = (datetime.now() - before)
        print delta.total_seconds()
        return ans
    return _func
