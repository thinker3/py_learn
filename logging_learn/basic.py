#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

root = logging.root

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    filename='basic.warn.log',
    filemode='w',
)
# root.setLevel(logging.ERROR)

warn_handler = root.handlers[0]
warn_handler.setLevel(logging.WARN)

error_handler = logging.FileHandler(
    'basic.error.log',
    mode='w',
)
error_handler.setLevel(logging.ERROR)
root.addHandler(error_handler)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
root.addHandler(console)

logging.debug('debug')
logging.info('info')
logging.warn('warn')
logging.error('error')
logging.fatal('fatal')

root.debug('debug')
root.info('info')
root.warning('warning')
root.error('error')
root.critical('critical')
