import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../src/main/python')))

import unittest

from calculator_Reina_Hani import add, subtract, multiply, divide, modulus, power, square_root


class TestCalculator(unittest.TestCase):
    # checks adding two numbers
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    # checks subtracting two numbers
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    # checks multiplying two numbers
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    # checks dividing, and that dividing by zero gives an error
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

    # checks the remainder, and that modulus by zero gives an error
    def test_modulus(self):
        self.assertEqual(modulus(10, 3), 1)
        self.assertEqual(modulus(9, 3), 0)
        self.assertEqual(modulus(-7, 3), 2)
        with self.assertRaises(ValueError):
            modulus(10, 0)

    # checks powers including zero, negative and fraction exponents
    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(9, 0.5), 3)

    # checks square roots, and that negative numbers give an error
    def test_square_root(self):
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(0), 0)
        self.assertAlmostEqual(square_root(2), 1.41421356, places=6)
        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == '__main__':
    unittest.main()
