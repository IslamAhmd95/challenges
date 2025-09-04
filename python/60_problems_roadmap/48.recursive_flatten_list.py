"""
Problem:
    Write a function flatten_list(lst) that recursively flattens a nested list.
"""

def flatten_list(lst, flat_list=None):  # Always use None then initialize inside the function.

    if flat_list is None:
        flat_list = []

    for i in lst:

        if isinstance(i, list):
            flatten_list(i, flat_list)  # we don't use return here, just recall the function again
        else:
            flat_list.append(i)

    return flat_list



print(flatten_list([1, [2, [3, 4], 5], 6]))

print(flatten_list([1, [2]]))

print(flatten_list([3, [4]]))
