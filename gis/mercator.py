#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from utils.math_utils import truncate_float

constant = 20037508.3427892


def lnglat_to_mercator(lng, lat):
    x = lng * constant / 180
    y = math.log(math.tan((90 + lat) * math.pi / 360)) / (math.pi / 180)
    y = y * constant / 180
    n = 1
    x = truncate_float(x, n)
    y = truncate_float(y, n)
    return x, y


def mercator_to_lnglat(x, y):
    lng = x / constant * 180
    lat = y / constant * 180
    lat = 180 / math.pi * (2 * math.atan(math.exp(lat * math.pi / 180)) - math.pi / 2)
    n = 6
    lng = truncate_float(lng, n)
    lat = truncate_float(lat, n)
    return lng, lat


lng, lat = 116.324662, 39.961028
print(lng, lat)
x, y = lnglat_to_mercator(lng, lat)
print(x, y)
print(mercator_to_lnglat(x, y))
