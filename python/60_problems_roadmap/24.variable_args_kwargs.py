"""
Problem:
    Write a function that accepts any number of positional and keyword arguments and prints or returns them in an organized format.
"""

from functools import reduce

def func(*args, **kwargs):

    if not args or not kwargs:
        return "Function requires at least one positional and one keyword argument."
    

    args_nums = list(filter(lambda x: isinstance(x, (int, float)) and not isinstance(x, bool), args))   # get numbers only from args

    square_args = list(map(lambda x: x ** 2, args_nums))

    args_chars = list(filter(lambda x:  isinstance(x, str) and len(x) == 1, args))

    combine_args_chars = reduce(lambda acc, curr: acc + curr, args_chars, "")

    person_keys = list(kwargs.keys())
    person_values = list(kwargs.values())

    full_str = ""
    for i in range(0, len(person_keys)):
        full_str += f"Person's {person_keys[i].capitalize()} is {person_values[i]}"  
        if i != len(person_keys) - 1:
            full_str += ", "


    return {
        "args_nums": args_nums or "No numbers provided",
        "square_args": square_args or "No numbers provided",
        "args_chars": args_chars or "No valid single-character strings",
        "args_chars_combined": combine_args_chars or "No valid single-character strings",
        "person_info": full_str
    }


result = func(1.5, 2, 3, 'i', 's', 'l', 'a', 'm', 'bla', None, name="islam", age=30, height=192)
print(result)

result = func(1.5, True, None, name="John")
print(result)
