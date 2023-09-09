# utils_tests.py
#ECE444 Assignment 1: Activity 4 - Nicholas Heeralal

import unittest
from utils import Utils

class Untils_Test(unittest.TestCase):

    # Test the reversed method with input that is an integer
    def test_reversed_integer(self):
        self.assertEqual(Utils.reversed(12345), 54321)

    # Test the reversed method with input that is a string
    def test_reversed_string(self):
        with self.assertRaises(Exception) as context:
            Utils.reversed("12345")
        self.assertEqual(str(context.exception), "Exception, reversed method did not receive an int")

    # Test the reversed method with input that is a float
    def test_reversed_float(self):
        with self.assertRaises(Exception) as context:
            Utils.reversed(4.44)
        self.assertEqual(str(context.exception), "Exception, reversed method did not receive an int")

    # Test the formatter method with input that is an integer
    def test_formatter_integer(self):
        self.assertEqual(Utils.formatter(444), {"binary": '0b110111100', "octal": '0o674'})

    # Test the formatter method with input that is a string
    def test_formatter_string(self):
        with self.assertRaises(Exception) as context:
            Utils.formatter("444")
        self.assertEqual(str(context.exception), "Exception, formatter method did not receive an int")

    # Test the formatter method with input that is a float
    def test_formatter_float(self):
        # Test with a float input
        with self.assertRaises(Exception) as context:
            Utils.formatter(4.44)
        self.assertEqual(str(context.exception), "Exception, formatter method did not receive an int")

if __name__ == '__main__':
    unittest.main()