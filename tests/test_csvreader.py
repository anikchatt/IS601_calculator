import unittest
from src.CsvReader import CsvReader, ClassFactory
from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.csv_reader = CsvReader('test_data/Unit Test Addition.csv')

    def test_return_data(self):
        testdata = self.csv_reader.return_objects('testdata')
        self.assertIsInstance(testdata, list)
        test_class = ClassFactory('testdata', self.csv_reader.data[0])

        for row in testdata:
            self.assertEqual(row.__name__, test_class.__name__)
            pprint(vars(row))

        if __name__ == '__main__':
            unittest.main()