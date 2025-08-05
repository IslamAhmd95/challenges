"""
Problem:
    Write a generator function fibonacci(limit) that yields Fibonacci numbers up to the given limit.
"""


def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a+b


n = 10

print(list(fibonacci(n)))

print("_"*60)

fib = fibonacci(n)
for i in fib:
    print(i)

print("_"*60)

fib = fibonacci(n)
while True:
    try:
        value = next(fib)
        print(value)
    except StopIteration:
        print("All values are processed")
        break



