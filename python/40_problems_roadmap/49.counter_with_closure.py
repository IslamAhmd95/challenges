"""
Problem:
    Write a function make_counter() that returns a function that counts up by 1 every time it’s called.
"""

def make_counter():
    counter = 0
    def increment():
        nonlocal counter
        counter += 1
        return counter
    return increment

counter = make_counter()
print(counter())
print(counter())
print(counter())
print(counter())