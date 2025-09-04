"""
Problem:
    Write a recursive function that collects all even numbers from a list of integers, including from any nested lists, and returns them in a flat list.
"""

def collect_even(nested):
    result = []
    for x in nested:
        if isinstance(x, list):
            result += collect_even(x)  # Combine returned values from inner calls
        elif isinstance(x, int) and x % 2 == 0:
            result.append(x)     # Collect even numbers
    return result


nested = [1, [2, 3, [4, 5]], 'a', ['c', 'b'], 6, [7, [8, [9, 10]]]]
result = collect_even(nested)
print(result)



"""
Notes:
    - Each recursive call creates its own `result` list.
    - We don’t lose previous progress because we return results and combine them.
    - ✅ Recursive return value logic:

        Even if we create a new variable (like result) inside each recursive call, it's not a problem.

        Each function call finishes its work and **returns** a value (like a small list).  
        The function that called it can **receive** that returned value and **add it** to its own result.

        This way, we build the final result step by step, from the deepest call back up to the first one.

"""