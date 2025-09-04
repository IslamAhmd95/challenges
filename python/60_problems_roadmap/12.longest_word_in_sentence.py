"""
Problem:
    Find the longest word in a given sentence. If multiple words have the same maximum length, return the first one.
"""


sentence = "The quick brown fox jumps over the lazy dog"
words = sentence.split()


# first solution
sorted_words = sorted(words, key= lambda item: len(item), reverse=True)
longest_word = sorted_words[0]
print(longest_word)


# second solution
word_length_map = {word: len(word) for word in words}
sorted_words = sorted(word_length_map.items(), key= lambda item: item[1], reverse=True)   # .items() returns an iterable of (key, value) tuples — great for sorting dicts.
longest_word = sorted_words[0][0]
print(longest_word)


# third solution
max_len = 0
longest_word = ""

for index, word in enumerate(words):
    if len(word) > max_len:
        max_len = len(word)
        longest_word = word

print(longest_word)



"""
Notes:
    - The third solution is a better solution that the first 2 due to:
        - Time complexity is O(n) — most efficient.
        - Always returns the first longest word.
        - Memory efficient — no need to store or sort all words.
        - Best choice for large input or performance-critical use.

    - The second solution is not efficient if the sentence has duplicated words — dictionary keys must be unique.

    - The first and the second solutions have a time complexity of O(n log n)
"""