"""
Problem:
    Find the single missing number in a list of integers within a given consecutive range.
"""

# missing single number
numbers = [1, 2, 3, 4, 5, 9, 7, 6, 10]
numbers_sorted = sorted(numbers)

for i in range(numbers_sorted[0], numbers_sorted[-1]+1):
    if i not in numbers_sorted:
        print(f"The missing single number in {numbers} list is: {i}")
        break


#--------------------------------------------------------------------


# missing multiple numbers
numbers = [1, 2, 4, 9, 6, 10]
numbers_sorted = sorted(numbers)
missing_numbers = []

for i in range(numbers_sorted[0], numbers_sorted[-1]+1):
    if i not in numbers_sorted:
        missing_numbers.append(i)

str_missing_numbers = map(str, missing_numbers)
print(f"The missing numbers in {numbers} list is: {", ".join(str_missing_numbers)}")