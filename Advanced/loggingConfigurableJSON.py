import logging
import logging.config
import json,sys

config = {
    'version':1,
    'root':{
        'level':'INFO',
        'propagate':"False",
        'handlers':[]
    },
    'loggers':{
        'simpleExample':{
            'level':'DEBUG',
            'propagate':"False",
            'handlers':['console']
        },
    },
    'formatters':{
        'simpleFormatter':{
            'format':'%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt':'%m/%d/%Y %I:%M:%S %p',}
    },
    'handlers':{
        'console':{
            'class':'logging.StreamHandler',
            'level':'DEBUG',
            'formatter': 'simpleFormatter',
            'stream':'ext://sys.stdout'
        },
    },
    'Incremental':False,
}

# 'application' code
def testMessages(logC):
    logC.debug('debug message')
    logC.info('info message')
    logC.warn('warn message')
    logC.error('error message')
    logC.critical('critical message')

if __name__ == '__main__':
    logging.raiseExceptions=True
    logging.lastResort = None
    logging.config.dictConfig(config)
    logger = logging.getLogger('simpleExample')
    testMessages(logger)
    config['handlers']['console']['stream'] = 'ext://sys.stderr'
    with open('loggingConfig.json', 'w') as f:
        f.write(json.dumps(config, indent=2))
    logging.config.dictConfig(json.load(open('loggingConfig.json')))
    logger = logging.getLogger('simpleExample')
    testMessages(logger)

