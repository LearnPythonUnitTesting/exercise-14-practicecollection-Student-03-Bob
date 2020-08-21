import unittest
from practice03 import get_score


class TestDemo(unittest.TestCase):

    def test_get_score(self):
        self.assertTrue(get_score('3jdi*44J82'),35)
        self.assertDictEqual(get_score('ue*2lds(2&'),57)
        self.assertEqual(get_score('d(2k&1J243'),50)
