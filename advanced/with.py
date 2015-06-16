#!/usr/bin/env python
# encoding: utf-8


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
    print fn
    print fn([1, 2, 3])
print fn
print fn([1, 2, 3])
