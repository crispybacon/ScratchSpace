import logging, sys

logger = logging.getLogger(__name__)
# set level
logger.setLevel(logging.DEBUG)
#create a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add a formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# application code
logger.debug('debug messsage')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
