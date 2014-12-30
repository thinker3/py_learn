#!/usr/bin/env python
# encoding: utf-8

import logging


def get_logger(time_stamp):
    # the root logger is created with level WARNING
    if time_stamp:
        # https://docs.python.org/2/library/logging.html#logging.basicConfig
        # This function does nothing if the root logger already has handlers configured for it
        logging.basicConfig(format='[%(asctime)s] %(levelname)s: %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(message)s', level=logging.DEBUG)
    return logging

# TypeError: info() takes at least 1 argument
#get_logger(time_stamp=True).info('hello')
#get_logger(time_stamp=False).info('')


def get_logger(time_stamp):
    if time_stamp:
        logger = logging.getLogger('time_stamp')
        formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    else:
        logger = logging.getLogger('empty_line')
        formatter = logging.Formatter('%(message)s')
    '''
    # or use singleton handlers
    if logger.handlers:
        return logger
    '''
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

get_logger(time_stamp=True).info('hello')
get_logger(time_stamp=False).info('')
get_logger(time_stamp=True).info('world')
get_logger(time_stamp=False).info('')
get_logger(time_stamp=True).info('what happened?')

handler = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
handler.setFormatter(formatter)


def get_logger_with_singleton_handler():
    logger = logging.getLogger('singleton')
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

get_logger_with_singleton_handler().info('hello')
get_logger_with_singleton_handler().info('world')
