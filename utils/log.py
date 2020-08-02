#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from logging import handlers

from . import config

_addHandler = logging.Logger.addHandler
_handle = logging.Handler.handle


def addHandler(self, hdlr):
    hdlr.name = self.name
    hdlr.logger = self
    return _addHandler(self, hdlr)


def handle(self, record):
    record.name = self.name
    return _handle(self, record)


logging.Logger.addHandler = addHandler
logging.Handler.handle = handle


def get_logger(name, propagate=False):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.propagate = propagate
    if not logger.handlers:
        formatter = logging.Formatter(config.LOG_FORMAT)
        handler = handlers.RotatingFileHandler(
            config.LOG_FILE_PATH,
            maxBytes=1024 * 1024 * 1,  # 1M
            backupCount=5,
        )
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
