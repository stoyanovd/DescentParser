import unittest
from helpers import Parser


class SoloOperation(unittest.TestCase):
    def test_add(self):
        cases = {'+ 2 4': 6, '+ 0 2': 2, '+ 0 0': 0, '+ 434 66': 500, '+ 3 5': 8}
        for s, r in cases.items():
            self.assertEqual(Parser.string_to_result(s), r)

    def test_sub(self):
        cases = {'- 2 4': -2, '- 0 2': -2, '- 0 0': 0, '- 434 66': 368, '- 3 5': -2}
        for s, r in cases.items():
            self.assertEqual(Parser.string_to_result(s), r)

    def test_mul(self):
        cases = {'* 2 4': 8, '* 0 2': 0, '* 0 0': 0, '* 434 66': 28644, '* 3 5': 15}
        for s, r in cases.items():
            self.assertEqual(Parser.string_to_result(s), r)
