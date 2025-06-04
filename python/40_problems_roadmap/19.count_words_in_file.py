"""
Problem:
    Write a program that reads a text file and counts the number of words in it.
"""
import os
import re

content_to_write = """
Python is a powerful programming language.
It is widely used in web development, data science, and automation.
This file is just a simple test.
"""

folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "sample.txt")

with open(file_path, 'w') as f:
    f.write(content_to_write)

with open(file_path, 'r') as f:
    content = f.read()

cleaned_content = re.sub(r'[^A-Za-z\s]', "", content)
words = cleaned_content.split()
print(f"Total words: {len(words)}")




"""
Notes:

    - [^A-Za-z\s] removes all characters except:
            - A-Z and a-z: so it keeps uppercase and lowercase letters
            - \s: keeps all whitespace (spaces, tabs, newlines)
    - So punctuation like . , ; ! etc. gets removed.
    - split() splits on any whitespace, so it handles multiple spaces or newlines correctly.
"""