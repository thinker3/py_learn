#!/usr/bin/env python
# -*- coding: utf-8 -*-

from blinker_test import custom_signal


@custom_signal.connect
def callback(sender, **kwargs):
    print sender
