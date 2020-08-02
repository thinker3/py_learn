#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import mercantile
from geopy.distance import great_circle


def degree2tile(lng, lat, zoom):
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    xtile = int((lng + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return (xtile, ytile)


def tile2degree(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lng = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat = math.degrees(lat_rad)
    return (lng, lat)


zoom = 22
# chongqing
lng, lat = 106.516034, 29.543124
print(lng, lat)
tile = mercantile.tile(lng, lat, zoom)
print(tile)
print(mercantile.ul(*tile))
box = mercantile.bounds(*tile)
print(box)
distance = great_circle((lat, box.west), (lat, box.east))
print(distance.meters, 'm')
distance = great_circle((box.north, lng), (box.south, lng))
print(distance.meters, 'm')

# beijing
lng, lat = 116.324662, 39.961028
xtile, ytile = degree2tile(lng, lat, zoom)
print(lng, lat)
print(xtile, ytile)
print(tile2degree(xtile, ytile, zoom))
box = mercantile.bounds(xtile, ytile, zoom)
print(box)
distance = great_circle((lat, box.west), (lat, box.east))
print(distance.meters, 'm')
distance = great_circle((box.north, lng), (box.south, lng))
print(distance.meters, 'm')
