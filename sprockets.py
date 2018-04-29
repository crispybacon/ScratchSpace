import logging
import logging.config
import json

def writeText(message, color=0):
    '''color codes text.  Range of 0-7'''
    return "\033[1;3{};50m{}\033[1;37;50m".format(color, message)

def loadConfigName(configName, configFile):
    '''Loads a configuration file in JSON format and selects a logger by name'''
    logging.raiseExceptions = True
    logging.lastResort = None
    with open(configFile) as f:
        data = f.read()
    logging.config.dictConfig(json.loads(data))
    return logging.getLogger(configName)