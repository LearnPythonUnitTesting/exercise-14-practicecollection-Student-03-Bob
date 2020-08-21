import unittest
from practice04 import get_fac


class TestDemo(unittest.TestCase):

    def test_get_fac(self):
        self.assertRaises(get_fac(2), 2)
        self.assertGreater(get_fac(3), 6)
        self.assertEqual(get_fac(4), 34)