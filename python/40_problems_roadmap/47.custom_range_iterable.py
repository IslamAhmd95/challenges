"""
Problem:
    Implement a class CustomRange(start, end) that mimics Python’s built-in range() but using your own iterator.
"""

class CustomRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration("Stop here")
        value = self.current
        self.current += 1
        return value



range = CustomRange(1, 5)
print(next(range))
print(next(range))
print(next(range))
print(next(range))
# print(next(range))  this raises a stopiteration exception

print("_"*60)

for i in CustomRange(2, 7):
    print(i)




"""
Notes:
    1. To make a class iterable:
        - Implement __iter__() that returns an iterator.

    2. To make a class an iterator:
        - Implement both __iter__() and __next__().
        - __iter__() should return self.

    3. 
        | Feature                 | Iterable                                                            | Iterator                                                 |
        | ----------------------- | ------------------------------------------------------------------- | -------------------------------------------------------- |
        | Implements `__iter__()` | ✅ Yes                                                               | ✅ Yes                                                    |
        | Implements `__next__()` | ❌ No                                                                | ✅ Yes                                                    |
        | Use case                | Can be looped over with `for` or `in`                               | Produces values one-by-one on demand                     |
        | Examples                | `list`, `dict`, `str`, `set`, custom classes with only `__iter__()` | Generators, file objects, iterators returned by `iter()` |

    4.
        class MyIterator:
            def __iter__(self):
                return self  # It’s its own iterator
            def __next__(self):
                # return next item or raise StopIteration
"""