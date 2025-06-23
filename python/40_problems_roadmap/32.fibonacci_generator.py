"""
Problem:
    Create a generator function generate_fibonacci(n) that yields the first n numbers of the Fibonacci sequence one by one, starting from 0.
    - Fibonacci sequence:
    0, 1, 1, 2, 3, 5, 8, 13, ...
    (Each number is the sum of the previous two)
"""


def generate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b

for num in generate_fibonacci(7):
    print(num)