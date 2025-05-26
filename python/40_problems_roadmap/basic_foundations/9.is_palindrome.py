"""
Problem:
    A Python program to check if a given string is a palindrome (reads the same forwards and backwards), ignoring spaces and case.
"""


import re

word = "Nurses Run"
word = re.sub(r'[^a-z0-9]', '', word.lower()) # removing spaces, punctuation or any special characters


# word = "Nurses Run".lower().strip().replace(' ', '')


# first solution
if word == word[::-1]:
    print("The given string is palindrome")
else:
    print("The given string is not palindrome")


# second solution
reverse_index = -1
for index, char in enumerate(word):
    if char != word[reverse_index]:
        print("The given string is not palindrome")
        exit()
    
    reverse_index -= 1

print("The given string is palindrome")

