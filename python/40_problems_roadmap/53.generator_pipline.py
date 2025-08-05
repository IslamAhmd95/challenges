"""
Problem:
    Build a data pipeline using generators:
        - generate_numbers(n)
        - filter_even(nums)
        - square(nums)
"""

def square_numbers_decorator(func):
    def wrapper(*args, **kwargs):
        for num in func(*args, **kwargs):
            if isinstance(num, int):
                yield num ** 2
    return wrapper

def filter_even_decorator(func):
    def wrapper(*args, **kwargs):
        for num in func(*args, **kwargs):
            if num % 2 == 0:
                yield num
    return wrapper



## Applying decorator
@square_numbers_decorator
@filter_even_decorator
def generate_numbers(n):
    for i in range(n):
        yield i


for i in generate_numbers(5):
    print(i)



## regular closure way without decorators
# functionally equivalent to using decorators — but instead of applying the decorators with @, you're applying them manually by wrapping one function with another.
def numbers_generator(n):
    for i in range(n):
        yield i


evens = filter_even_decorator(numbers_generator)
squares = square_numbers_decorator(evens)
for i in squares(5):
    print(i)




"""
Notes:

    1. Decorators are applied from bottom to top, so:

            filter_even_decorator is applied first to number_generator.

            square_numbers_decorator is applied second, and wraps the output of the filtered results.

        This means:

            filter_even_decorator filters the even numbers from number_generator using yield — one value at a time (memory efficient).

            square_numbers_decorator takes the filtered values and squares them — also using yield.

        The final result is:
            → generate numbers from 0 to n-1,
            → filter only the even ones,
            → then square them.

        Decorators can change the behavior of the return values of the decorated function, especially when using yield for lazy evaluation.


    2. generate_numbers(n) yields numbers from 0 to n - 1.

    3. filter_even is a higher-order function that yields only even numbers.

    4. square_even is another higher-order function that squares each even number.

    5. Each wrapper returns a generator — making the whole process lazy and memory efficient.
"""