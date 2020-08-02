#!/usr/bin/env python
# -*- coding: utf-8 -*-


def amplified(a, b):
    return 1/(1 - a *b), a / (1 - a * b), (1 - a) / (1 - a * b)


print(amplified(0.75, 0.9))
print(amplified(0.9, 0.9))
print(amplified(0.999, 0.999))
