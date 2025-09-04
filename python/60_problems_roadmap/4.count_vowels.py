"""
Problem:
    Write a Python program that counts the number of vowels in a given string.
    Vowels include: a, e, i, o, u (both uppercase and lowercase).
    For example, the input "Hello World" should return 3 vowels.
"""

word = input("Enter the string to count vowels: ").strip().lower()

count = 0
vowels = {'a', 'e', 'i', 'o', 'u'}
count = sum(1 for l in word if l in vowels)

print(f"'{word}' has {count} vowels.")


"""
Notes:
    1. Sets have O(1) lookup time while lists have O(n), this comes down to how they store data internally:
        - List Lookup – O(n)
            - A list is an ordered collection of items stored in sequence.
            - When you check if x in some_list, Python checks each element one by one from the start.
            - In the worst case, the item is at the end or not in the list at all, so Python checks all items.
            - Example:
                vowels = ['a', 'e', 'i', 'o', 'u']
                if 'u' in vowels:
                    # Python checks 'a', then 'e', ..., then 'u'
            - Time complexity: O(n) where n = number of items in the list.

        - Set Lookup – O(1)
            - A set is an unordered collection implemented using a hash table.
            - When you check if x in some_set, Python hashes the value and goes directly to the memory "bucket" where that value would be stored.
            - So, it doesn't scan all elements — it jumps straight to the right location.
            - Example:
                vowels = {'a', 'e', 'i', 'o', 'u'}
                if 'u' in vowels:
                    # Python calculates the hash of 'u' and checks only that bucket
            - Time complexity: O(1) on average, because hashing gives direct access.
"""