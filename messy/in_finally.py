#!/usr/bin/env python
# -*- coding: utf-8 -*-


def test_return_in_finally(divisor):
    try:
        if 10 > divisor > -10:
            return 60 / divisor
    except Exception:
        return 'except'
    else:
        return 'else'
    finally:
        return 'finally'


def test_not_return_in_finally(divisor):
    try:
        if 10 > divisor > -10:
            return 60 / divisor
    except Exception:
        return 'except'
    else:
        return 'else'
    finally:
        print 'finally'


assert test_return_in_finally(0) == 'finally'
assert test_return_in_finally(2) == 'finally'
assert test_return_in_finally(12) == 'finally'

assert test_not_return_in_finally(0) == 'except'
assert test_not_return_in_finally(2) == 30
assert test_not_return_in_finally(12) == 'else'
