import unittest
from src.calculator import Calculator
from src.CsvReader import CsvReader

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_addition_calculator(self):
        test_data = CsvReader('test_data/Unit Test Addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction_calculator(self):
        test_data = CsvReader('test_data/Unit Test Subtraction.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_multiply_calculator(self):
        test_data = CsvReader('test_data/Unit Test Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 2'], row['Value 1']), result)
            self.assertEqual(self.calculator.result, result)

    def test_divide_calculator(self):
        test_data = CsvReader('test_data/Unit Test Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.divide(row['Value 2'], row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_sq_calculator(self):
        test_data = CsvReader('test_data/Unit Test Square.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.square(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)

    def test_sq_rt_calculator(self):
        test_data = CsvReader('test_data/Unit Test Square Root.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertAlmostEqual(self.calculator.sq_rt(row['Value 1']), result)
            self.assertAlmostEqual(self.calculator.result, result)


    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()
