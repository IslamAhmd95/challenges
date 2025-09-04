"""
Problem:
    Write a function that calculates the total time (in milliseconds) it takes to type a number on a keyboard using only one finger, assuming:

    Steps: 
        - You start at key '0'
        - Every move between two digits takes 1 millisecond per unit distance
        - The keyboard layout is defined by the string digits, which gives the linear left-to-right layout
        - For each digit in the number to type, calculate how far your finger has to move from its current position to reach it
"""


digits = "8425391706"
nums = "210"

if not digits or not nums:
    raise ValueError("Both digits and num can't be empty.")

if not digits.isdigit() or not nums.isdigit():
    raise ValueError("Both digits and nums values have to be digit values.")

if len(set(digits)) != len(digits):
    raise ValueError("Digits layout must contain unique values.")

count = 0
last_num_index = 0

for num in nums:

    if num not in digits:
        raise ValueError(f"{num} doesn't exist in digits")
    
    digit_pos = {d: i for i, d in enumerate(digits)}
    current_num_index = digit_pos[num]
    count += abs(current_num_index - last_num_index)
    last_num_index = current_num_index

print(count)