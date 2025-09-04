"""
Problem:
    Write a Python function to calculate the factorial of a number using recursion.
    The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n.
    For example, 5! = 5 × 4 × 3 × 2 × 1 = 120
"""

def calculate_factorial(number):
    if number == 0 or number == 1:
        return 1
    
    return number * calculate_factorial(number - 1)


while True:
    number = input("Enter a number to calculate the factorial (or type 'q' to exit): ")

    if number.lower() == 'q':
        break

    try:
        number = int(number)

        if number < 0:
            print("Factorial is not defined for negative numbers.\n")
            continue

        factorial = calculate_factorial(number)
        print(f"{number}! is {factorial}.\n")

    except ValueError as e:
        print("Invalid input. Please enter a valid integer.\n")



"""
Notes:
    1. Recursion Basics
        A recursive function must always have:
            - A base case (when to stop).
            - A recursive case (calls itself with a smaller input).

    2. Factorial Function
        - Base case: factorial(1) should return 1.
        - Recursive case: factorial(n) = n * factorial(n - 1)
"""