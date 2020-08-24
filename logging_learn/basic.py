#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


class NoErrorFilter(logging.Filter):
    def filter(self, record):
        assert self.name == 'x'
        assert self.nlen == 1
        return record.levelno < 40


class StopFilter(logging.Filter):
    def filter(self, record):
        assert self.name == 'yy'
        assert self.nlen == 2
        if record.getMessage() == 'stop':
            return False
        return True


root_logger = logging.root
assert root_logger.level == logging.WARNING == 30
assert root_logger.filters == []
assert root_logger.handlers == []
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s %(levelname)s]: %(message)s',
    filename='basic.warn.log',
    filemode='w',
)
assert root_logger.level == logging.INFO == 20
assert root_logger.filters == []
assert len(root_logger.handlers) == 1
print(root_logger.handlers)
basic_handler = root_logger.handlers[0]
assert basic_handler.level == logging.NOTSET == 0
basic_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('[%(asctime)s %(levelname)s]> %(message)s')
error_handler = logging.FileHandler(
    'basic.error.log',
    mode='w',
)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)
root_logger.addHandler(error_handler)
assert len(root_logger.handlers) == 2

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)
console_handler.addFilter(NoErrorFilter('x'))
console_handler.addFilter(StopFilter('yy'))
assert len(console_handler.filters) == 2
root_logger.addHandler(console_handler)
assert len(root_logger.handlers) == 3

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.fatal('fatal')
logging.info('stop')

root_logger.debug('debug')
root_logger.info('info')
root_logger.warning('warning')
root_logger.error('error')
root_logger.critical('critical')
root_logger.info('go through')
