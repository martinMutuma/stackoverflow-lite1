import unittest
from app import stolite
from app.config import *

from app.tests import db_setUp, db_teardown


class TestSample(unittest.TestCase):
    def setUp(self):
        db_setUp()

    def tearDown(self):
        # db_teardown()
        pass

    def test_sample(self):
        assert True
  