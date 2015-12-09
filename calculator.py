class Calculator:
    def __init__(self):
        self.base_numeral_system = 10

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            raise ZeroDivisionError
        return x / y

    def evaluate(self, expression):
        try:
            result = eval(expression)
        except:
            raise SyntaxError
        return result

