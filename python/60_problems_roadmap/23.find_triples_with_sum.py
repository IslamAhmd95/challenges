"""
Problem:
    Given a list of integers and a target number, find all unique triplets (three numbers) in the list that add up to the target sum. Each triplet must contain distinct indices, and no duplicate triplets are allowed (e.g., [1, 2, 2] and [2, 1, 2] are the same).
"""
from collections import Counter

numbers = [1, 2, -1, 0, -2, 1, -1]
target = 0

numbers_counter = Counter(numbers)
seen = set()
unique_triples = []

for first_num in numbers_counter:
    for second_num in numbers_counter:

        third_num = target - (first_num + second_num)

        triplet = sorted([first_num, second_num, third_num]) 
        triplet_key = frozenset(triplet)
        if triplet_key in seen:
            continue

        #  This block makes sure we really have enough of each number from the triplet in the original list
        triplet_counter = Counter(triplet)
        is_valid = all(numbers_counter[num] >= triplet_counter[num] for num in triplet_counter)
        if is_valid:
            unique_triples.append(triplet)
            seen.add(triplet_key)

print(unique_triples)