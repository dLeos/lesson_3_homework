class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def float_exec(self, x, y, z):
        try:
            float(x - y)
            return z(x, y)
        except:
            raise SyntaxError

    def add(self, x, y):
        """This function adds two numbers"""
        return self.float_exec(x, y, lambda x, y: x + y)

    def subtract(self, x, y):
        """This function subtracts two numbers"""
        return self.float_exec(x, y, lambda x, y: x - y)

    def multiply(self, x, y):
        """This function multiplies two numbers"""
        return self.float_exec(x, y, lambda x, y: x * y)

    def divide(self, x, y):
        """This function divides two numbers"""
        if y == 0:
            raise ZeroDivisionError
        return self.float_exec(x, y, lambda x, y: x / y)

    def evaluate(self, expression):
        """This function evaluate expression"""
        try:
            return eval(expression)
        except:
            raise SyntaxError

