import unittest
from app  import stolite
from app.config import *

class TestConfigs(unittest.TestCase):
    def test_main_configs(self):
        stolite.config.from_object(Config)
        self.assertEqual(stolite.config['DEBUG'], False)

    def test_development_config(self):
        stolite.config.from_object(DevelopmentConfig)
        self.assertEqual(stolite.config['DEBUG'], True)

        