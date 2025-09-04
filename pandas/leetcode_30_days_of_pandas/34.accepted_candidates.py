"""
Problem:
    - Name: Accepted Candidates From the Interviews
    - Write a query to find candidate_ids of candidates who:
    - Have at least 2 years of experience (years_of_exp >= 2)
    - Have a total interview score (sum of all their round scores) strictly greater than 15
"""

import pandas as pd


def sales_person(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    candidates_scores = candidates[candidates['years_of_exp'] >= 2][['candidate_id', 'interview_id']].merge(rounds[['interview_id', 'score']], on='interview_id')
    agg_candidates_scores = candidates_scores.groupby('candidate_id').agg(
        total_score = ('score', 'sum')
    ).query('total_score > 15').reset_index()
    return agg_candidates_scores[['candidate_id']]


candidates = pd.DataFrame([
    {"candidate_id": 11, "name": "Atticus", "years_of_exp": 1,  "interview_id": 101},
    {"candidate_id": 9,  "name": "Ruben",   "years_of_exp": 6,  "interview_id": 104},
    {"candidate_id": 6,  "name": "Aliza",   "years_of_exp": 10, "interview_id": 109},
    {"candidate_id": 8,  "name": "Alfredo", "years_of_exp": 0,  "interview_id": 107},
])

rounds = pd.DataFrame([
    {"interview_id": 109, "round_id": 3, "score": 4},
    {"interview_id": 101, "round_id": 2, "score": 8},
    {"interview_id": 109, "round_id": 4, "score": 1},
    {"interview_id": 107, "round_id": 1, "score": 3},
    {"interview_id": 104, "round_id": 3, "score": 6},
    {"interview_id": 109, "round_id": 1, "score": 4},
    {"interview_id": 104, "round_id": 4, "score": 7},
    {"interview_id": 104, "round_id": 1, "score": 2},
    {"interview_id": 109, "round_id": 2, "score": 1},
    {"interview_id": 104, "round_id": 2, "score": 7},
    {"interview_id": 107, "round_id": 2, "score": 3},
    {"interview_id": 101, "round_id": 1, "score": 8},
])

print(sales_person(candidates, rounds))