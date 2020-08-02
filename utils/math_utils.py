#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import decimal


def truncate_float(f, n=2):
    # 3.14159 -> 3.14
    return math.floor(f * 10 ** n) / 10 ** n


def round_down_float(f, n=2):  # truncate and fill zeros if needed
    places = decimal.Decimal('0.1') ** n
    return decimal.Decimal(str(f)).quantize(places, decimal.ROUND_DOWN)


if __name__ == '__main__':
    print(round_down_float(3.1))
    print(round_down_float(3.14159, 4))
