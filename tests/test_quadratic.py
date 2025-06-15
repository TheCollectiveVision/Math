import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quadratic_formula.main import solve_quadratic


class TestQuadraticFormula(unittest.TestCase):
    def test_known_equation(self):
        roots = solve_quadratic(1, -5, 6)
        self.assertCountEqual(roots, (3.0, 2.0))

    def test_no_real_roots(self):
        roots = solve_quadratic(1, 0, 1)
        self.assertEqual(roots, (None, None))

    def test_zero_a_coefficient(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 1)


if __name__ == "__main__":
    unittest.main()
