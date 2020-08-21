import unittest
from practice05 import fizzBuzz


class TestDemo(unittest.TestCase):

    #numbers that are exact multiples of 3, or that contain 3, return a string "Fizz"
    #numbers that are exact multiples of 5, or that contain 5, return a string "Buzz"
    def test_fizz(self):
        self.assertEqual(fizzBuzz(3), 'Fizz')
        self.assertEqual(fizzBuzz(5), 'Buzz')
        self.assertEqual(fizzBuzz(6), 'Fizz')
        self.assertEqual(fizzBuzz(13), "Fizz")
        self.assertEqual(fizzBuzz(15), 'FizzBuzz')
        self.assertEqual(fizzBuzz(16), '16')
        self.assertEqual(fizzBuzz(21), 'Fizz')
        self.assertEqual(fizzBuzz(30), 'FizzBuzz')
        self.assertEqual(fizzBuzz(44), '44')
