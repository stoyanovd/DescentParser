import unittest
from helpers import Parser


class PlainNumbers(unittest.TestCase):
    def test_one_digit(self):
        cases = ['0', '1', '7']
        for d in cases:
            self.assertEqual(Parser.string_to_result(d), int(d))

    def test_semi_digit_1(self):
        cases = ['12', '343', '2452525', '543442424']
        for d in cases:
            self.assertEqual(Parser.string_to_result(d), int(d))
