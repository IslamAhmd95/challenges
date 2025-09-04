"""
Problem:
    Create a generator function called custom_range(start, end, step=1) that behaves like Python’s built-in range(), but returns a generator (not a list).
    It should yield numbers from start to end (exclusive), increasing by step.
"""

def custom_range(start, end, step=1):
    current = start
    while current < end:
        yield current
        current += step

gen = custom_range(3, 10, 2)
for num in gen:
    print(num)


print("-" * 50)


gen2 = custom_range(2, 10)

print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
for num in gen2:
    print(num)
