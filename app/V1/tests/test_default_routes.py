import unittest
from app  import stolite
from app.config import *

class TestDefaultRoutes(unittest.TestCase):
    def setUp(self):
        stolite.config.from_object(DevelopmentConfig)
        self.testApp = stolite.test_client()

    def test_all_routes_list(self):
        response = self.testApp.get(
            '/api/v1/'
        )
        assert b'/test' in response.data
        assert b'/' in response.data
