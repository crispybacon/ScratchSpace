from sprockets import writeText, loadConfigName

if __name__ == '__main__':
    logger = loadConfigName('simpleExample', 'loggingConfig.json')
    for i in range(8):
        logger.info(writeText('Configuration Loaded!', i))