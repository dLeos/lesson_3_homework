from unittest import TestCase
from calculator import Calculator
import unittest

class CalculatorTest(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(12, self.calc.add(5, 7))

    def test_subtract(self):
        self.assertEqual(-2, self.calc.subtract(5, 7))

    def test_multiply(self):
        self.assertEqual(35, self.calc.multiply(5, 7))

    def test_divide(self):
        self.assertEqual(float(5/7), self.calc.divide(5, 7))

    def test_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: self.calc.divide(5, 0))

    def test_evaluate(self):
        self.assertEqual(5, self.calc.evaluate("(5+7*5)/2**3"))

    def test_evaluate_error(self):
        self.assertRaises(SyntaxError, lambda: self.calc.evaluate("sin(PI)"))

if __name__ == '__main__':
    unittest.main()
