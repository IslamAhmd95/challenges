"""
Problem:
    Given an unsorted list of integers that should represent a consecutive range, find all the missing numbers.
"""


def validate_list(numbers):
    # remove not-integer items
    integer_numbers = [x for x in numbers if isinstance(x, int)]
    # removes duplicates and gives a sorted list
    return sorted(set(integer_numbers))


def get_missing_numbers(validated_numbers):
    if len(validated_numbers) < 2:
        return []
    
    start = validated_numbers[0]
    end = validated_numbers[-1]
    full_range = set(range(start, end+1))
    existing_numbers = set(validated_numbers)
    return sorted(full_range - existing_numbers)


numbers = [10, 4, 1, 2, 2, 6, 9, 'c', 'd']
validated_numbers = validate_list(numbers)
missing_numbers = get_missing_numbers(validated_numbers)

if len(missing_numbers) == 0:
    print("No Missing numbers")
    exit()

print(f"The missing numbers in {numbers} list are: {', '.join(map(str, missing_numbers))}")
