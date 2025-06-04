"""
Problem:
    Implement a custom version of the built-in split() function that splits a string into a list of substrings based on a given delimiter.
"""

string = "apple,banana,cherry".strip().replace(" ", "")
delimiter = ","

string_list = []
substring = ""

for char in string:

    if char == delimiter:
        string_list.append(substring)
        substring = ""
    else:
        substring += char
    
if substring:
    string_list.append(substring)

print(string_list)




"""
Notes:
    - Group related lines together, and separate unrelated logic with blank lines.
    - Use blank lines inside large blocks to separate mini-tasks.
        for char in string:
            # Skip leading spaces
            if char == " " and not substring:
                continue

            # Handle delimiter
            if char == delimiter:
                if substring:
                    string_list.append(substring)
                substring = ""
                continue

            # Add char to current substring
            substring += char
"""