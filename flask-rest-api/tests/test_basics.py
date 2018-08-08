import unittest

from flask import current_app

class BasicsTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_that_passes(self):
        self.assertTrue(True)