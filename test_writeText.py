from unittest import TestCase
from sprockets import writeText, loadConfigName

class TestWriteText(TestCase):
    def test_writeText(self):
        self.logger = loadConfigName('simpleExample', 'loggingConfig.json')
        self.failUnlessEqual(self.logger.info(writeText('Configuration Loaded!', 4)),None)
