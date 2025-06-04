"""
Problem:
    Use list comprehension to flatten a nested list (a list of lists) into a single flat list.
"""

nested_list = [[1, 2], [3, 4], [5, 6]]

flat_list = [y for x in nested_list for y in x]
print(flat_list)


#------------------------------------------------------------------------


def flatten_list(nested_list):
    result = []
    for x in nested_list:
        if isinstance(x, list):
            result += flatten_list(x)
        else:
            result.append(x)
    
    return result

nested_list = [1, [2, [3, 4], 5], 6, [7, [8, [9]]]]
result = flatten_list(nested_list)
print(result)


#--------------------------------------------------------------------------


def flatten_list(nested):
    result = []  # Start a new result list in each function call

    for x in nested:
        if isinstance(x, list):
            result += flatten_list(x)
        elif x is not None:
            result.append(x)

    return result


nested = [1, ['a', [None, 2, ['b']], 3], None, ['c', [4, [5]]]]
print(flatten_list(nested))


"""
Notes:
    1. Avoid passing an external list to collect results

        Passing an external list (e.g., flat_list) into a recursive function creates side effects.

        It makes the function impure: same input may produce different outputs depending on external state.

        It also makes reuse harder and debugging more difficult.

        Better practice:
            Create and return a new list inside each function call, then combine results on return.

    2. Local result list in recursion — why it works

        Each recursive call creates its own fresh result = [] list.

        This local list stores flattened elements for that call only.

        When the function hits a nested list, it calls itself recursively, which returns a flattened sublist.

        The sublist is then added to the current call’s result using result += flatten_list(sublist).

        This process builds the full flattened list step-by-step bottom-up.

        Because every call’s result is independent, lists don’t overwrite each other.

    3. Difference from resetting a list inside a loop

        If you define a list inside a loop, it resets every iteration, losing previous data.

        In recursion, each call’s list is reset once, but calls don’t overwrite each other — they build on each other when returning.
"""