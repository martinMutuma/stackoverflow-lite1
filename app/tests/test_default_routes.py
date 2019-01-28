import unittest
from app  import stolite
from app.config import *

class TestMainAppDefaultRoutes(unittest.TestCase):
    def setUp(self):
        stolite.config.from_object(DevelopmentConfig)
        self.testApp = stolite.test_client()

    def test_all_routes_list(self):
        response = self.testApp.get(
            '/'
        )
        assert b'/api/v1/' in response.data
        assert b'/' in response.data
