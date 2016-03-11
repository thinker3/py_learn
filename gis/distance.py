#!/usr/bin/env python
# -*- coding: utf-8 -*-

from geopy.distance import vincenty
from geopy.distance import great_circle

newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
distance = vincenty(newport_ri, cleveland_oh)
print(distance.kilometers)
import ipdb; ipdb.set_trace()
distance = great_circle(newport_ri, cleveland_oh)
print(distance.kilometers)
