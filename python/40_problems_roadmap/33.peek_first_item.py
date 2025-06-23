"""
Problem:
    Write a function that takes any iterable or iterator and returns the first item along with a full iterator that still includes all the items (including the first one). The function should not lose or consume any item.
"""

import itertools

def peek_iter(iter):
    a_iter, b_iter = itertools.tee(iter, 2)
    return next(a_iter), b_iter


result = peek_iter(['a', 'b', 'c'])
first, it = result
print("First item:", first)
for val in it:
    print("Remaining:", val)
