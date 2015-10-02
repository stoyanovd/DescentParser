import unittest
from helpers import Parser


class FewOperations(unittest.TestCase):
    def test_1(self):
        cases = {'+ * 2 4 3': 11, '- + 2 3 + 0 2': 3, '+ 0 * 1 0': 0,
                 '- - - 4 2 1 8': -7, '* + 3 5 10': 80}

        for s, r in cases.items():
            self.assertEqual(Parser.string_to_result(s), r)
