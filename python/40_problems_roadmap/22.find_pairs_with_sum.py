"""
Problem:
    Find all unique pairs of numbers in a list that add up to a given target sum.
"""
from collections import Counter

numbers = [1, 3, 2, 2, 4, 5, 1, 4]
target = 5

# numbers = [2, 2, 3]  
# target = 4

numbers_counter = Counter(numbers)
seen = set()
unique_pairs = []

for num in numbers_counter:

    second_num = target - num

    pair_key = frozenset([num, second_num])
    # frozenset([2, 3]) = frozenset([3, 2])
    if pair_key in seen:
        continue

    # Without checking numbers_counter[2] >= 2, you might falsely consider (2, 2) as valid even when there's only one 2.
    if (num == second_num and numbers_counter[num] >= 2) or (second_num in numbers_counter):
        unique_pairs.append(tuple(sorted(num, second_num)))
    

    seen.add(pair_key)

print(unique_pairs)



"""
Notes:
    - Handles duplicates correctly

        - It uses Counter to track the frequency of each number.

        - It checks for (2, 2) only if it appears at least twice.

    - Avoids duplicate pairs like (2, 3) and (3, 2)

        - Thanks to frozenset([num, second_num]), which treats both as the same key.

    - Efficient lookup

        - Uses dictionary (Counter) and set for O(1) average time checks.


    - What is Counter?
        Counter from collections is a subclass of dict that counts how many times each item appears in a list.

    - Why is it efficient?
    
        Both:

            num in numbers_counter

            pair_key in seen

        are dictionary or set lookups, which use hash tables internally.

        This means:

        Looking up an item (e.g., 2 in numbers_counter) has average time complexity of O(1) — constant time.

        Much faster than scanning a list, which would take O(n).
"""