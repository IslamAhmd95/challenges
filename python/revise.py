## 1. Strings

# Reverse a string without using slicing ([::-1]).
s = 'hello'
reverse_s = ''
for i in range(len(s) - 1, -1, -1):
    reverse_s += s[i]

print(reverse_s)


# Count vowels in a string.
vowels_count = 0
vowels = ['e', 'a', 'i', 'o', 'u']
s_set = set(s)
for char in s_set:
    if char in vowels:
        vowels_count += 1

print(vowels_count)


# Remove all punctuation from a string.
import string

s = '@gel!e,l.'
clean_s = "".join([char for char in s if char not in string.punctuation])
print(clean_s)


# Check if two strings are anagrams (same letters in any order).
def check_anagrams(s1, s2):
    s1_to_list = sorted(list(s1))
    s2_to_list = sorted(list(s2))

    if s1_to_list == s2_to_list:
        print("both strings are anagrams")
    else:
        print("both strings are not anagrams")


s1 = 'erfucne'
s2 = 'fuencer'
check_anagrams(s1, s2)

s1 = 'erfunc'
s2 = 'fuencer'
check_anagrams(s1, s2)


## 2.Numbers

# Write a function to check if numbers in a list is prime.
import math

def check_prime(l):
    d = dict()

    for num in l:

        if num < 1:
            raise ValueError('Prime can\'t be less than 1')

        if num in [1, 2, 3]:
            d[num] = 'Prime'
            continue

        if num % 2 == 0:
            d[num] = 'Not Prime'
            continue

        d[num] = 'Prime'
        for i in range(3, math.floor(num/2)+1, 2):
            if num % i == 0:
                d[num] = 'Not Prime'
                break
    
    return d

print(check_prime([1, 3, 7, 2, 9, 15, 8]))


# Find the sum of digits of a number.
from functools import reduce

l = [1, 3, 7, 2, 9, 15, 8]
total = reduce(lambda acc, curr: acc + curr, l, 0)
print(total)


# Generate the first 10 multiples of a given number.
import math
def generate_multiples(num):

    count = 1
    multiples = [1]

    for i in range(2, math.floor(num/2) + 1):
        if num % i == 0:
            multiples.append(i)
            count += 1

            if count == 10:
                break

    return multiples

print(generate_multiples(5000))
