#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def truncate_float(f, n=2):
    # 3.14159 -> 3.14
    return math.floor(f * 10 ** n) / 10 ** n
