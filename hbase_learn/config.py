#!/usr/bin/env python
# -*- coding: utf-8 -*-


host = '172.18.0.5'

try:
    from local_config import *  # noqa
except Exception as e:
    print type(e), e
