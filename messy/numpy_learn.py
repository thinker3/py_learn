#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

a_array = np.array([0.1, 0.2, 0.3])
b_array = np.array([0.3, 0.2, 0.1])
c_array = a_array + b_array
print(c_array)

A = 10
A = 1
f = 1
sr = 20
duration = 2

x_array = np.arange(sr * duration) / sr
y_array = np.sin(2 * np.pi * f * x_array) * A
print(x_array)
print(y_array)
ints = np.int16(y_array * 32767)
print(ints)
