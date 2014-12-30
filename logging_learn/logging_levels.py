#!/usr/bin/env python
# encoding: utf-8

import logging


def levels():
    print logging.NOTSET  # 0
    print logging.DEBUG  # 10
    print logging.INFO  # 20
    print logging.WARN  # 30
    print logging.WARNING  # 30
    print logging.ERROR  # 40
    print logging.CRITICAL  # 50

levels()
