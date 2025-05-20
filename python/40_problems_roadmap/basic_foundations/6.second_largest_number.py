"""
Problem:
    Write a Python program to find the second largest number in a list of integers.
    The solution should work without using built-in sorting functions like sorted().
"""

# numbers = [12, 45, 3, 22, 89, 45]
# numbers = [5, 5, 5]
# numbers = [10]
# numbers = [-10, -20, -3, -5]
numbers = [100, 100, 99]

if len(numbers) < 2:
    print("List must contain at least two values to find a second largest.")
    exit()

first = None
second = None

for num in numbers:
    if first is None or num > first:
        second = first
        first = num
    elif num < first and (second is None or num > second):
        second = num

if second is not None:
    print("Second largest number is: ", second)
else:
    print("There is no second largest number (all values are equal).")



"""
Notes:

    Edge cases are special or unusual inputs that can break your code if you don’t handle them.
    They are not common, but they are important to test.

        📌 Simple Examples:
            If you're writing code to find the second largest number in a list:
                - A list with only one number → Example: [5]
                - A list where all numbers are the same → Example: [3, 3, 3]
                - A list with only negative numbers → Example: [-2, -5, -1]
                - A list with two numbers only → Example: [10, 5]

    These are edge cases because they are different from normal cases, and your code must handle them correctly.
"""