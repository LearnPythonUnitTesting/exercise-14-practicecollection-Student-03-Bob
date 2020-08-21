import unittest
from practice01 import  add

class TestDemo(unittest.TestCase):

    def test_add(self):
        assert add(10, 5) == 15

    def test_subtract(self):
        #TODO

    def test_multiply(self):
        #TODO