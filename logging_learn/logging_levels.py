#!/usr/bin/env python
# encoding: utf-8

import logging


def test_levels():
    assert logging.NOTSET == 0
    assert logging.DEBUG == 10
    assert logging.INFO == 20
    assert logging.WARN == 30
    assert logging.WARNING == 30
    assert logging.ERROR == 40
    assert logging.FATAL == 50
    assert logging.CRITICAL == 50


def test_parent():
    root_logger = logging.getLogger()
    assert root_logger is logging.root
    assert isinstance(root_logger, logging.RootLogger)
    a = logging.getLogger('a')
    b = logging.getLogger('a.b')
    assert isinstance(a, logging.Logger) and isinstance(b, logging.Logger)
    assert a.parent == a.root == root_logger
    assert b.parent.parent == b.root == root_logger


def test_root_logger_basic_config():
    root_logger = logging.getLogger()
    logging.basicConfig()
    assert root_logger.level == logging.WARNING
    assert len(root_logger.handlers) == 1
    handler = root_logger.handlers[0]
    assert handler.level == logging.NOTSET
    assert isinstance(handler, logging.StreamHandler)
    return handler


def test_root_logger_basic_config_file_handler(handler):
    root_logger = logging.getLogger()
    root_logger.removeHandler(handler)
    assert root_logger.info is not logging.info
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M',
        filename='test.log',
        filemode='w',
    )
    assert root_logger.level == logging.DEBUG
    assert len(root_logger.handlers) == 1
    handler = root_logger.handlers[0]
    assert isinstance(handler, logging.FileHandler)
    return handler


def test_root_logger_basic_config_order(handler):
    root_logger = logging.getLogger()
    root_logger.removeHandler(handler)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    root_logger.addHandler(console)
    assert len(root_logger.handlers) == 1
    root_logger.info('hello')  # ???
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M',
        filename='test.log',
        filemode='w',
    )
    assert len(root_logger.handlers) == 1


test_levels()
test_parent()
handler = test_root_logger_basic_config()
handler = test_root_logger_basic_config_file_handler(handler)
test_root_logger_basic_config_order(handler)
