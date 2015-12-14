class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
        """This function adds two numbers"""
        try:
            return float(x + y)
        except:
            raise SyntaxError

    def subtract(self, x, y):
        """This function subtracts two numbers"""
        try:
            return float(x - y)
        except:
            raise SyntaxError

    def multiply(self, x, y):
        """This function multiplies two numbers"""
        try:
            return float(x * y)
        except:
            raise SyntaxError

    def divide(self, x, y):
        """This function divides two numbers"""
        if y == 0:
            raise ZeroDivisionError
        try:
            return float(x / y)
        except:
            raise SyntaxError

    def evaluate(self, expression):
        """This function evaluate expression"""
        try:
            return eval(expression)
        except:
            raise SyntaxError

