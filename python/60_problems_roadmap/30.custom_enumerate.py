"""
Problem:
    Recreate Python’s built-in enumerate() function.
    It should take an iterable and return a list (or generator) of pairs:
    (index, item) — optionally starting from a custom start value.

    You can make it:
        - Return a list → for simplicity
        - Return a generator → more advanced & memory efficient
"""

# regular list way
def custom_enumerate(items, start=0):

    enumerated_list = []
    counter = start

    for item in items:
        enumerated_list.append((counter, item))
        counter += 1

    return enumerated_list


items = ['apple', 'banana', 'cherry']
print(custom_enumerate(items))

items = ['x', 'y', 'z']
print(custom_enumerate(items, start=5))


# first generator way
items = ['apple', 'banana', 'cherry']
items_gen = (item for item in items)
start = 0
for item in items_gen:
    print(start, item)
    start += 1



# second generator way
def custom_generator(items, start=0):
    counter = start
    for item in items:
        yield(counter, item)
        counter += 1

for i, val in custom_enumerate(items):
    print(i, val)