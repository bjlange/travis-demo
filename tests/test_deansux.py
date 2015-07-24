import unittest
import deansux

class DeanTests(unittest.TestCase):
    def test_type(self):
        self.assertIsInstance(deansux.run(), str)
    def test_content(self):
        self.assertIs(deansux.run(), "hello")
