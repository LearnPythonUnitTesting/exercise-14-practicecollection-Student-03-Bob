import unittest
from practice02 import generate_array


class TestDemo(unittest.TestCase):

    def test_generate_array(self):
        self.assertEqual(generate_array(2, 5), [2, 3, 4])
        self.assertEqual(generate_array(4, 8), [4, 5, 6, 7])
