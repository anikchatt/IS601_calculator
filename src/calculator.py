from .addition import addition
from .division import division
from .multiplication import multiplication
from .square_root import square_root
from .squared import squared
from .subtraction import subtraction



class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a,b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a,b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a,b)
        return self.result

    def divide(self, a, b):
        self.result = division(a,b)
        return self.result

    def square(self, a):
        self.result = squared(a)
        return self.result

    def sq_rt(self, a):
        self.result = square_root(a)
        return self.result

