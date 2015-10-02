import unittest
from helpers import Parser
from helpers.LexicalAnalyzer import ParseException
from helpers.Parser import BadTokenException


class BadCases(unittest.TestCase):
    def test_bad_token(self):

        cases = [
            '+ * 2 4',
            '- + 2  + 0 2']

        for s in cases:
            self.assertRaises(BadTokenException, Parser.string_to_result, s)

    def test_bad_symbol(self):

        cases = [
            '+ 0 & 1 0',
            '* + 3 5 a 0',
            '* + 3 5a 0']
        for s in cases:
            self.assertRaises(ParseException, Parser.string_to_result, s)
