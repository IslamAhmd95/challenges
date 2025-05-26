"""
Problem:
    Write a Python program to remove duplicate values from a list while preserving the original order.
"""

l = [5, 1, 2, 2, 3, 4, 4, 4, 5]  

## Set way without preserving the original order
# unique_l = list(set(l))
# print(unique_l)


## Dict way
# y = 0
# d = dict.fromkeys(l, y)
# print(list(d.keys()))


## manual way
l = [1, 2, 2, 3, 2]
unique_l = []

for item in l:
    if item not in unique_l:
        unique_l.append(item)    

print(unique_l)


"""
Notes:
    - new_l = l : new_l is referencing the same list in memory, so changes to one affect the other.
    - new_l = l.copy() is a shallow copy of the original list `l`.
    - Using `set(l)` removes duplicates but does **not** preserve the original order.
    - Using `dict.fromkeys(l)` (Python 3.7+) removes duplicates **and** preserves order (because dicts preserve insertion order).
"""
