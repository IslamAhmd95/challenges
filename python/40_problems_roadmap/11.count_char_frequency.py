"""
Problem:
    A Python program to count the frequency of each character in a given string.
"""

import re
from collections import Counter

word = "hello world"
word = re.sub(r'[^a-z ]', '', word.lower())  # Removes all characters except lowercase letters and spaces.


# manual solution
char_frequency = dict()

for char in word:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(char_frequency)


#-------------------------------------------------------------------------------------


# using collection module
print(dict(Counter(word)))

