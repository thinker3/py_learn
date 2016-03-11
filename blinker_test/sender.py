#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blinker import signal
from blinker import Namespace
from blinker_test import custom_signal

print custom_signal is signal('custom')
signal = Namespace().signal
print custom_signal is signal('custom')

custom_signal.send('Tom')
