#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

_random = random.random


def my_random():
    return 'random.random changed'

random.random = my_random
print(random.random())

from import_learn import reloaded_or_not
reloaded_or_not.random = random  # inject something into a module's global namespace
reloaded_or_not.is_random_reloaded()
print reloaded_or_not.math.pi
print reloaded_or_not.math.e
print reloaded_or_not.math.factorial(5)


def run_with_python3():
    import importlib  # python3
    importlib.reload(random)
    print(random.random())


def run_with_python2():
    reload(random)
    print(random.random())

run_with_python2()
# run_with_python3()
