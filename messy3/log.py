#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging.config
from logging import handlers
from utils import config

from utils.log import get_logger
root_logger = logging.getLogger()

assert root_logger is logging.root
assert root_logger.name == 'root'
assert root_logger.parent is None
assert root_logger.root is root_logger
assert root_logger.filters == []
assert root_logger.handlers == []
assert root_logger.hasHandlers() is False
assert root_logger.disabled is False
assert root_logger.propagate is True
assert isinstance(root_logger.manager, logging.Manager)

assert root_logger.level is logging.WARN
root_logger.setLevel(logging.ERROR)
assert root_logger.level is logging.ERROR

logging.basicConfig(
    level=logging.INFO,
    format=config.LOG_FORMAT,
    filename='root.log',
    filemode='w',  # default 'a'
)
assert root_logger.level is logging.INFO
assert root_logger.hasHandlers()

handler = root_logger.handlers[0]
assert isinstance(handler, logging.FileHandler)
assert handler.level is logging.NOTSET
assert handler.name == 'root'
assert handler.logger is root_logger
assert handler.filters == []
assert handler.delay is False
assert handler.encoding is None
assert handler.terminator == '\n'
assert isinstance(handler.formatter, logging.Formatter)

root_logger.info(handler.baseFilename)

#name = f'root.{__name__}'  # deoplete/jedi error
name = 'root.{name}'.format(name=__name__)
logger = get_logger(name, propagate=True)
assert logger.name == 'root.__main__'
assert logger.level is logging.DEBUG
assert logger.parent is logger.root is root_logger
assert logger.hasHandlers()

handler = logger.handlers[0]
formatter = handler.formatter
assert isinstance(handler, handlers.RotatingFileHandler)
assert handler.level is logging.DEBUG
assert handler.name == 'root.__main__'
assert handler.logger is logger

logger.info(handler.baseFilename)
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.error('stderr')
