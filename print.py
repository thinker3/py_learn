#!/usr/bin/env python
# pretty print

import pprint 

out = {'a':2, 'b':{'x':3, 'y':{'t1': 4, 't2':5}}}
pprint.pprint(out)
#pprint.pprint(out, width=0)  # AssertionError: width must be != 0
pprint.pprint(out, width=1)
