import unittest
from unittest import TestCase
from calculator import Calculator
from genty import genty, genty_dataset

@genty
class CalculatorTest(TestCase):
    def setUp(self):
        self.calc = Calculator()

    @genty_dataset((5, 7, 12), (5.1, 7.1, 12.2), (-5.1, 7.1, 2.0))
    def test_add_correct(self, x, y, result):
        self.assertEqual(result, self.calc.add(x, y))

    @genty_dataset(('ab', 7, SyntaxError), (5, 'cd', SyntaxError), ('ab', 'cd', SyntaxError))
    def test_add_not_correct(self, x, y, result):
        self.assertRaises(result, lambda: self.calc.add(x, y))

    @genty_dataset((5, 7, -2), (5.1, 7.1, -2.0), (-5.1, 7.9, -13))
    def test_subtract_correct(self, x, y, result):
        self.assertEqual(result, self.calc.subtract(x, y))

    @genty_dataset(('ab', 7, SyntaxError), (5, 'cd', SyntaxError), ('ab', 'cd', SyntaxError))
    def test_subtract_not_correct(self, x, y, result):
        self.assertRaises(result, lambda: self.calc.subtract(x, y))

    @genty_dataset((5, 7, 35), (5.1, 7.1, 36.21), (-5.1, 7.1, -36.21))
    def test_multiply_correct(self, x, y, result):
        self.assertAlmostEqual(result, self.calc.multiply(x, y))

    @genty_dataset(('ab', 7, SyntaxError), (5, 'cd', SyntaxError), ('ab', 'cd', SyntaxError))
    def test_multiply_not_correct(self, x, y, result):
        self.assertRaises(result, lambda: self.calc.multiply(x, y))

    @genty_dataset((5, 7, float(5/7)), (5.1, 7.1, float(5.1/7.1)), (-5.1, 7.1, -float(5.1/7.1)))
    def test_divide_correct(self, x, y, result):
        self.assertAlmostEqual(result, self.calc.divide(x, y))

    @genty_dataset(('ab', 7, SyntaxError), (5, 'cd', SyntaxError), ('ab', 'cd', SyntaxError))
    def test_divide_not_correct(self, x, y, result):
        self.assertRaises(result, lambda: self.calc.divide(x, y))

    @genty_dataset((5, 0, ZeroDivisionError), (7.1, 0, ZeroDivisionError))
    def test_division_by_zero(self, x, y, result):
        self.assertRaises(result, lambda: self.calc.divide(x, y))

    @genty_dataset(("(5+7*5)/2**3", 5), ("5&3", 1), ("5^3", 6), ("5|3", 7))
    def test_evaluate_correct(self, expression, result):
        self.assertEqual(result,  self.calc.evaluate(expression))

    @genty_dataset(("sin(PI)", SyntaxError), (")2+3(", SyntaxError))
    def test_evaluate_not_correct(self, expression, result):
        self.assertRaises(result, lambda: self.calc.evaluate(expression))

if __name__ == '__main__':
    unittest.main()
