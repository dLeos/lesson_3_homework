class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
        """This function adds two numbers"""
        try:
            result = float(x + y)
        except:
            raise SyntaxError
        return result

    def subtract(self, x, y):
        """This function subtracts two numbers"""
        try:
            result = float(x - y)
        except:
            raise SyntaxError
        return result

    def multiply(self, x, y):
        """This function multiplies two numbers"""
        try:
            result = float(x * y)
        except:
            raise SyntaxError
        return result

    def divide(self, x, y):
        """This function divides two numbers"""
        if y == 0:
            raise ZeroDivisionError
        try:
            result = float(x / y)
        except:
            raise SyntaxError
        return result

    def evaluate(self, expression):
        """This function evaluate expression"""
        try:
            result = eval(expression)
        except:
            raise SyntaxError
        return result

