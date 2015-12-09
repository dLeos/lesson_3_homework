from calculator import Calculator

calc = Calculator()

def read_number():
    number = input("Enter first number: ")
    try:
        number = float(number)
    except ValueError:
        raise ValueError
    return number

while True:
    print("Menu:\n"
          "1. Add\n"
          "2. Substract\n"
          "3. Multiply\n"
          "4. Divide\n"
          "5. Evaluate\n"
          "0. Exit\n")

    action = input("What do you want? ")

    if action == '0':
        break

    elif action == '5':
        expression = input("Enter the expression: ")
        try:
            result = calc.evaluate(expression)
        except SyntaxError:
            print("Error: incorrect expression.\n")
            continue

    else:
        try:
            x = read_number()
            y = read_number()
        except ValueError:
            print("Error: incorrect number")
            continue

        if action == '1':
            result = calc.add(x, y)
        if action == '2':
            result = calc.subtract(x, y)
        if action == '3':
            result = calc.multiply(x, y)
        if action == '4':
            try:
                result = calc.divide(x, y)
            except ZeroDivisionError:
                print("Error: incorrect number")
                continue
    print("Result: ", result)

