import io
import unittest
from tests.simple_text import PlainNumbers, SoloOperation, FewOperations, BadCases


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.makeSuite(PlainNumbers.PlainNumbers))
    s.addTests(unittest.makeSuite(SoloOperation.SoloOperation))
    s.addTests(unittest.makeSuite(FewOperations.FewOperations))
    s.addTests(unittest.makeSuite(BadCases.BadCases))
    return s


if __name__ == '__main__':
    # unittest.main()
    unittest.TextTestRunner(verbosity=2).run(suite())
