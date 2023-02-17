import math
while True:
    try:
        operation = input("Enter operation To Perform (+, -, *, /, ^, sqrt, sin, cos, tan): ")
        if operation in ['+', '-', '*', '/']:
            num1 = float(input("Enter First number: "))
            num2 = float(input("Enter Second number: "))
        elif operation in ['^']:
            num1 = float(input("Enter Base: "))
            num2 = float(input("Enter Exponent: "))
        elif operation in ['sqrt']:
            num1 = float(input("Enter Number: "))
        else:
            num1 = float(input("Enter angle (in degrees): "))
            num1 = math.radians(num1)

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        elif operation == "^":
            result = num1 ** num2
        elif operation == "sqrt":
            result = math.sqrt(num1)
        elif operation == "sin":
            result = math.sin(num1)
        elif operation == "cos":
            result = math.cos(num1)
        elif operation == "tan":
            result = math.tan(num1)
        else:
            print("Invalid operation")
            continue
        print("Result: ", result)

    except ValueError:
        print("Invalid input, please enter a number.")
        continue

    except ZeroDivisionError:
        print("Cannot divide by zero.")
        continue
    else:
        break
