"""
Problem:
    Write a Python program to merge two dictionaries into a single dictionary. If there are overlapping keys, the second dictionary’s value should overwrite the first’s.
"""

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# union way
merged_dict = dict1 | dict2
print(merged_dict)

# unpacking way
merged_dict = {**dict1, **dict2}
print(merged_dict)

# using update
dict1.update(dict2)  # merge the 2 dicts into `dict1`
print(dict1)
