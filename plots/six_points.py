#!/usr/bin/env python
# encoding: utf-8

import math
import matplotlib.pyplot as plt

plt.scatter(
    [math.sin(p)*50 for p in [x*(math.pi/3) for x in range(6)]],
    [math.cos(p)*50 for p in [x*(math.pi/3) for x in range(6)]],
)
plt.axis('scaled')
plt.show()
