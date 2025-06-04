"""
Problem:
    Implement a simple calculator that performs basic arithmetic operations (+, -, *, /, %, **, //) using if/else statements or the operator module.
"""

import argparse
import sys
import operator


class MyArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f"Custom error: {message}\n")
        self.print_help()
        sys.exit(2)


parser = MyArgumentParser(description="Calculator Program")

parser.add_argument("num1", type=float, metavar="First Number", help="first number")
parser.add_argument("num2", type=float, metavar="Second Number", help="second number")

# optional argument
# parser.add_argument("-o", "--operation", type=str, choices=["add", "subtract", "multiply", "divide"], default="add", help="The operation to perform. Choices: add, subtract, multiply, divide (default: add)")

# positional argument
parser.add_argument("operation", type=str, choices=["add", "subtract", "multiply", "divide", "remainder", "power", "floorDiv"],  help="The operation to perform. Choices: add, subtract, multiply, divide, remainder, power, floor division")

args = parser.parse_args()
num1 = args.num1
num2 = args.num2
operation = args.operation

if operation in ["divide", "remainder", "floorDiv"] and num2 == 0:
    print("The Second Number can't be zero")
    exit()


symbol_map = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/",
    "remainder": "%",
    "power": "**",
    "floorDiv": "//"
}
symbol = symbol_map[operation]


# solution using the operator module
operations = {
    "add": operator.add,
    "subtract": operator.sub,
    "multiply": operator.mul,
    "divide": operator.truediv,
    "remainder": operator.mod,
    "power": operator.pow,
    "floorDiv": operator.floordiv
}


result = operations[operation](num1, num2)
print(f"{num1} {symbol} {num2} = {result}")


#---------------------------------------------------------------------------------


# if/else solution
if operation.lower() == 'add':
    result = num1 + num2
elif operation.lower() == 'subtract':
    result = num1 - num2
elif operation.lower() == 'multiply':
    result = num1 * num2
elif operation.lower() == 'divide':
    result = num1 / num2
elif operation.lower() == 'remainder':
    result = num1 % num2
elif operation.lower() == 'power':
    result = num1 ** num2
elif operation.lower() == 'floorDiv':
    result = num1 // num2

print(f"{num1} {symbol} {num2} = {result}")