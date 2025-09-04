"""
Problem:
    Given a list of words, group them in a dictionary by their starting letter.
"""

from collections import defaultdict


lst = ['apple', 'banana', 'apricot', 'blueberry', 'cherry']
group = defaultdict(list)

for word in lst:
    group[word[0]].append(word)


group_sorted = dict(sorted(group.items()))  # sorting by key is the default behavior of sorted(dict.items()), so you don’t need to specify it
print(group_sorted)



"""
Notes:
    1. defaultdict is a special type of dictionary from the collections module.

        - Unlike a regular dict, it automatically creates default values for missing keys — so you don’t get KeyError when accessing a key that doesn’t exist.

        - Syntax:
            from collections import defaultdict
            d = defaultdict(default_factory)

        - default_factory is a function that returns the default value for any new key.
            - defaultdict(list) → default value is an empty list: []
            - defaultdict(int) → default value is 0
            - defaultdict(set) → default value is an empty set: set()
"""

print("_"*60)

# Example on defaultdict
students = [
    ("Math", "Ali"),
    ("Science", "Sara"),
    ("Math", "Mona"),
    ("Science", "Omar")
]

# group = defaultdict(int)
group = defaultdict(list)

for subject, student in students:
    # group[subject] += 1  # to get number of students on each subject
    group[subject].append(student)

print(group)
print(group.items())  # we can use `items()` with `group` because it's also a dict