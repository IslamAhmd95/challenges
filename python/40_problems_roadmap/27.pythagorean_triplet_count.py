"""
Problem:
    Count all unique combinations of (i, j, k) such that i² + j² = k² and all values are less than or equal to a given number n.
"""

from math import isqrt

def solution(n: int) -> int:
    list_of_sets = []

    for i in range(2, n):
        for j in range (2, n):

            k_square = i ** 2 + j ** 2
            k = isqrt(k_square)

            if k * k == k_square and n >= k:
                list_of_sets.append((i, j, k))

    return list_of_sets


if __name__ == '__main__':
    n = int(input("Enter n: "))
    result = solution(n)
    print(result)