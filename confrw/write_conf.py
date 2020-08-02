#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser

config = configparser.SafeConfigParser()
filename = 'test.conf'
config.read(filename)
debug = config.getboolean('default', 'debug')
print(debug, type(debug))
debug = not debug
# ## TypeError: option values must be strings
# config.set('default', 'debug', debug)
config.set('default', 'debug', str(debug))
with open(filename, 'w') as configfile:
    config.write(configfile)
