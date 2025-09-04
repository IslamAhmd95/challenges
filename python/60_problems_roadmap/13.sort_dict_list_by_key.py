"""
Problem:
    Sort a list of dictionaries based on the value of a specified key.
"""
from operator import itemgetter

data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "Ahmed"}
]

data_sorted = sorted(data, key = lambda item : item.get('age', 0))
# data_sorted = sorted(data, key = lambda item : item['age'])
# data_sorted = sorted(data, key=itemgetter('age'))
print(data_sorted)


"""
Notes:
    - sorted() goes through each dictionary in the list (just like a loop).
    - Use .get(key, default) to avoid exceptions when keys may be missing.
    - Use itemgetter() when performance matters in large-scale data, but it will raise an error if the key "age" is missing
    - item[key] will also raise an error in case of key missing
"""