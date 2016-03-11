#!/usr/bin/env python
# encoding: utf-8


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


def isolate(*args, **kwargs):
    # @isolate, with or without ()
    if len(args) == 1 and callable(args[0]):
        return segregate(args[0])
    sep = kwargs.get('sep') or '*'
    length = kwargs.get('length') or 30
    return separate(sep, length)
