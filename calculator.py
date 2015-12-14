class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
        """This function adds two numbers"""
        return float(x + y)

    def subtract(self, x, y):
        """This function subtracts two numbers"""
        return float(x - y)

    def multiply(self, x, y):
        """This function multiplies two numbers"""
        return float(x * y)

    def divide(self, x, y):
        """This function divides two numbers"""
        if y == 0:
            raise ZeroDivisionError
        return float(x / y)

    def evaluate(self, expression):
        """This function evaluate expression"""
        try:
            return eval(expression)
        except:
            raise SyntaxError

