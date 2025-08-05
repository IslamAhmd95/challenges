"""
Problem:
    Create a closure function make_averager() that returns a function which keeps a running average of numbers passed to it.
"""


def make_averager():
    total = []
    def calculate_avg(number: int) -> float:
        # we do not need nonlocal in this specific case because total is a mutable object (a list), and we're only modifying it in-place using total.append(number). we're not reassigning it.
        total.append(number)
        return sum(total) / len(total)
    return calculate_avg


avg = make_averager()
print(avg(10))
print(avg(20))
print(avg(30))



"""
Notes:
    1. If the outer variable is a mutable object like (list, dict, set)
    …and you're only modifying the object (not reassigning it) inside the inner function (e.g., appending, updating, removing), then: You don’t need nonlocal.
    Because you’re not assigning a new object to the variable — you're mutating the existing one.

    2. When nonlocal is needed ?
        If you're dealing with immutable types like (int, float, str, tuple, bool)
        …and you're trying to reassign the variable in the inner function (e.g., count += 1, text = text + "abc"), then: You must use nonlocal, or you'll get UnboundLocalError.
"""