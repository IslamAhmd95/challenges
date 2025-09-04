#  Problem: Actors and Directors Who Cooperated At Least Three Times
#  Link: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    result = actor_director[['actor_id', 'director_id']].value_counts().reset_index()
    return result[result['count'] >= 3][['actor_id', 'director_id']]