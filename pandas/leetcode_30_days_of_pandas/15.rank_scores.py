#  Problem: Rank Scores
#  Link: https://leetcode.com/problems/rank-scores/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)
    return scores[['score', 'rank']].sort_values(by='score', ascending=False)



"""
Notes:
    1. Use astype() to convert series type
"""


scores = [
    [1, 2, 3, 4, 5, 6],
    [3.50, 3.65, 4, 3.85, 4, 3.65]
]

scores = tuple(zip(*scores))

scores_df = pd.DataFrame(scores, columns=['id', 'score'])

print(order_scores(scores_df))




