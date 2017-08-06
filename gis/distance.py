#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geopy.distance import vincenty
from geopy.distance import great_circle

# def __new__(cls, latitude=None, longitude=None, altitude=None):


def calc_distance():
    newport_ri = (41.49008, -71.312796)
    cleveland_oh = (41.499498, -81.695391)
    distance = vincenty(newport_ri, cleveland_oh)
    print(distance.kilometers)
    distance = great_circle(newport_ri, cleveland_oh)
    print(distance.kilometers)


# chongqing

start = (29.5441, 106.522128)
end = (29.5445, 106.522128)
distance = great_circle(start, end)
print(distance.meters)

start = (29.545, 106.5221)
end = (29.545, 106.5226)
distance = great_circle(start, end)
print(distance.meters)

# beijing

start = (39.8991, 116.407764)
end = (39.8995, 116.407764)
distance = great_circle(start, end)
print(distance.meters)

start = (39.8991, 116.4071)
end = (39.8991, 116.4076)
distance = great_circle(start, end)
print(distance.meters)
