"""
Problem:
    Write a Python program to reverse a string without using built-in functions like [::-1] or reversed().
    You should reverse the string manually using a loop.
"""

word = input("Please enter the word to reverse: ").strip()
# reverse_word = ''
reverse_word_list = []

for index in range(len(word) - 1, -1, -1):
    # reverse_word += word[index]
    reverse_word_list.append(word[index])

# print(reverse_word)
print(''.join(reverse_word_list))



"""
Notes:
    - Building a string with += in a loop works fine for small inputs, but is less efficient for large strings due to string immutability in Python.
    - For large-scale use, it's better to build a list and join it at the end.
"""