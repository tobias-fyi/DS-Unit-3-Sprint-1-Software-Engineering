"""The test file for square root functions, 'calc.py'"""

import unittest
from calc import lazy_sqrt, builtin_sqrt, newton_sqrt

# Our class for square root functions
class SqrtTests(unittest.TestCase):
    """These are our tests for square root funcs"""

    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)

    def test_newton_sqrt2(self):
        self.assertAlmostEqual(newton_sqrt(2), 1.414213562)


if __name__ == "__main__":
    unittest.main()
