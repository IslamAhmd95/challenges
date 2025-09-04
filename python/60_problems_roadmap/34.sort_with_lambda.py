"""
Problem:
    Write a function that sorts a list of dictionaries (or tuples, or strings) using sorted() with a lambda to define the custom sort key.
    You can sort by string length, a specific key, or by a calculated value.
"""

def sort_iterable(iterable, sort_key, reverse_val=False):
    return sorted(iterable, key=sort_key, reverse=reverse_val)


# Sort by string length:
items = ["apple", "banana", "kiwi", "blueberry"]
sorted_items = sort_iterable(items, lambda x: len(x))
print(sorted_items)

# Sort by dictionary key:
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 25}
]
sorted_people = sort_iterable(people, lambda x: x["age"])
print(sorted_people)

# Sort by nested dictionary key:
scores = [
    {"name": "Alice", "subjects": 
        {
            "math": 30,
            "science": 50
        }
    },
    {"name": "Bob", "subjects": 
        {
            "math": 10,
            "science": 20
        }
    },
    {"name": "Charlie", "subjects": 
        {
            "math": 70,
            "science": 40
        }
    }
]
sorted_scores = sort_iterable(scores, lambda x: (x['subjects']['math'], x['subjects']['science']), True)
print(sorted_scores)