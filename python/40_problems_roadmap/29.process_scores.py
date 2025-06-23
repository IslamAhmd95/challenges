"""
Problem:
    Given a list of student scores (as integers), do the following:
        - remove failing scores (e.g., below 50)
        - add 10 bonus points to the remaining scores (max score is 100)
        - calculate the total of all boosted scores
        - Return a summary dictionary with:
            (Original scores - Passed scores - Boosted scores - Final total)
"""
from functools import reduce


def boost_by_10(x):
    return min(x + 10, 100)


def process_scores(original):
    passed = list(filter(lambda x: x > 50, original))
    boosted = list(map(boost_by_10, passed))
    total = reduce(lambda acc, curr: acc + curr, boosted, 0)

    return {
        "original": original,
        "passed": passed,
        "boosted": boosted,
        "total": total
    }


scores = [45, 60, 72, 30, 88, 95, 43]
print(process_scores(scores))
