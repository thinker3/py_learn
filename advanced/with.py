#!/usr/bin/env python
# encoding: utf-8

import time
from functools import wraps


class AliasContextManager(object):
    # python context manager

    def __init__(self, fn):
        self.fn = fn

    def proxy(self):
        def _proxy(*args, **kwargs):
            fn = getattr(self, "fn", None)
            return fn(*args, **kwargs)
        return _proxy

    def __enter__(self):
        return self.fn
        return self.proxy()

    def __exit__(self, *args):
        pass
        del self.fn
        #self.fn = None


alias = AliasContextManager

with alias(sum) as fn:
    print(fn)
    print(fn([1, 2, 3]))
print(fn)
print(fn([1, 2, 3]))


class ContextDecorator(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, typ, val, traceback):
        print("{}: {}".format(self.label, time.time() - self.start_time))

    def __call__(self, f):
        self.label = f.__name__

        @wraps(f)
        def wrapper(*args, **kw):
            with self:
                return f(*args, **kw)
        return wrapper


@ContextDecorator(label='foo')
def loop():
    for i in range(10 ** 7):
        pass


loop()


def wait():
    for i in range(10 ** 8):
        pass


with ContextDecorator(label='bar'):
    wait()
