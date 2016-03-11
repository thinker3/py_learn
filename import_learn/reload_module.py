#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

_random = random.random


def my_random():
    return 1

random.random = my_random
print(random.random())


def run_with_python3():
    import importlib  # python3
    importlib.reload(random)
    print(random.random())


def run_with_python2():
    reload(random)
    print(random.random())

run_with_python2()
# run_with_python3()
