import csv
import os

def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)

class CsvReader:
    data = []

    def __init__(self, filepath):
        self.data = []

        with open(os.path.abspath(filepath)) as test_data:
            csv_data = csv.DictReader(test_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects
