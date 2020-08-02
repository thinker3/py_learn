#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def is_random_reloaded():
    # the first place checked during import search is sys.modules
    # import random  # not reloaded
    print(random.random())
