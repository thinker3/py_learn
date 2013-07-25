import logging

def show(level):
    root_logger = logging.getLogger()
    root_logger.setLevel(level)
    logging.info('info')
    logging.debug('debug')
    logging.warn('warn')
    logging.error('error')
    logging.fatal('fatal')
    logging.warning('warning')
    logging.critical('critical')
    logging.exception('exception')
    print '*' * 30

show(logging.WARNING)
show(logging.DEBUG)

