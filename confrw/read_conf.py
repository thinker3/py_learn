#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
from utils.decorators import isolate
from utils.functions import abs_path
from utils.functions import divide

config = configparser.SafeConfigParser()
filename = 'test.conf'
filename = abs_path(__file__, filename)
config.read(filename)
debug = config.get('default', 'debug')
print(debug, type(debug))
debug = config.getboolean('default', 'debug')
print(debug, type(debug))
port = config.getint('email', 'port')
print(port, type(port))

divide()
sections = config.sections()
for section in sections:
    print(section)
    for k, v in config.items(section):
        print('\t%s: %s' % (k, v))


class MyString(str):
    def to_int(self):
        return int(self)
    def to_float(self):
        return float(self)

divide()
s = MyString('1').to_int()
print(s)


class SecondLevel(object):
    def __init__(self, options):
        for k, v in options:
            setattr(self, k, MyString(v))


class MyConfigParser(configparser.SafeConfigParser):
    def __init__(self, *args, **kwargs):
        # ## TypeError: must be type, not classobj
        # super(MyConfigParser, self).__init__(*args, **kwargs)
        configparser.SafeConfigParser.__init__(self, *args, **kwargs)

    def init(self):
        for section in self.sections():
            options = self.items(section)
            second_level = SecondLevel(options)
            setattr(self, section, second_level)

@isolate
def test():
    config = MyConfigParser()
    config.read(filename)
    config.init()
    print(config.email.smtp)
    print(config.email.port.to_int())

divide()
test()
