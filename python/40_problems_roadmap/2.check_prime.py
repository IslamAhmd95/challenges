"""
Problem:
    Write a Python program that checks whether a given number is a prime number. A prime number is a number greater than 1 that has no divisors other than 1 and itself.
"""

import math

def check_prime(number):

    if number <= 1:
        return False
    elif number == 2:
        return True
    elif number % 2 == 0:
        return False
    
    for i in range(3, math.isqrt(number) + 1, 2):
        if number % i == 0:
            return False
        
    return True



while True:
    number = input("Enter a number to check (or type 'q' to exit): ")

    if number.lower() == 'q':
        break

    try:
        number = int(number)

        if check_prime(number):
            print(f"{number} is a prime number.\n")
        else:
            print(f"{number} is not a prime number.\n")

    except ValueError as e:
        print("Invalid input. Please enter a valid integer.\n")

    

"""
Notes:
    1. sqrt() vs isqrt()
        - sqrt(): Returns the float square root 
            Examples:
                math.sqrt(9)  # ➞ 3.0 (float)
                math.sqrt(10)  # ➞ 3.1622776601683795 (float)
        - isqrt(): Returns the integer square root, it never returns a float, always rounds down to the     nearest integer and introduced in Python 3.8+.
            Examples:
                math.isqrt(10)  # ➞ 3
                math.isqrt(16)  # ➞ 4
"""