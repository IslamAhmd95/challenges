"""
Problem:
    You need to count how many unique files contain the word "bull" and the word "bear" as separate words, not as substrings like "bullish" or "bearish".
my rate: medium
"""


import pandas as pd


Files = pd.DataFrame({
    'file_name': ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt'],
    'content': [
        'The market saw a bull trend today.',
        'Bear attacks are rare.',
        'The bull is strong. A bear followed it.',
        'People say bullish things.',
        'Bearish signs are not uncommon.'
    ]
})

count_occurrences = []

bull_count = Files['content'].str.contains('(^|\s)bull(\s|$)', case=False, regex=True).sum()
count_occurrences.append(['bull', bull_count])
bear_count = Files['content'].str.contains('(^|\s)bear(\s|$)', case=False, regex=True).sum()
count_occurrences.append(['bear', bear_count])

count_occurrences_df = pd.DataFrame(count_occurrences, columns=['word', 'count'])
print(count_occurrences_df)


"""
Notes:
    1. sum() counts the number of True values 
    2. nunique() counts how many distinct values exist (True, False, or NaN), not used for counting matches
    3. to_frame(name) — Convert Series to DataFrame
        - Converts a Series to a 1-column DataFrame.
        - Useful for debugging, inspecting, or merging later.
            EX: df['col'].str.contains(r'(^|\s)bear(\s|$)', case=False).to_frame('has_bear')
            OUTPUT: 
                has_bear
            0     False
            1      True
            2      True
            3     False
            4     False
"""

print("_"*60)

s = pd.Series(['cairo', 'luxor', 'aswan'], name='cities', index=['a', 'b', 'c'])
print(s)
print("_"*30)
f = s.to_frame('new_cities')
print(f)