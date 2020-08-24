#!/usr/bin/env python
# encoding: utf-8

import logging


def get_logger(timestamp):
    # the root logger is created with level WARNING
    if timestamp:
        # https://docs.python.org/2/library/logging.html#logging.basicConfig
        # This function does nothing if the root logger already has handlers configured for it
        logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    return logging

# TypeError: info() takes at least 1 argument
#get_logger(timestamp=True).info('hello')
#get_logger(timestamp=False).info('')


def get_logger(timestamp):
    if timestamp:
        logger = logging.getLogger('with-timestamp')
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    else:
        logger = logging.getLogger('without-timestamp')
        formatter = logging.Formatter('%(levelname)s: %(message)s')
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

get_logger(timestamp=True).info('hello')
get_logger(timestamp=False).info('hello')
get_logger(timestamp=True).info('world')
get_logger(timestamp=False).info('world')
