#  Problem: Game Play Analysis I
#  Link: https://leetcode.com/problems/game-play-analysis-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby('player_id', as_index=False).agg(
        first_login = ('event_date', 'min')
    )


# another solution
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.sort_values(['player_id', 'event_date']).groupby('player_id').head(1)[['player_id', 'event_date']].rename(columns={'event_date': 'first_login'})




"""
Notes:

    1. `as_index=False` means event_day and emp_id will stay as columns instead of becoming index, it's similar to using `reset_index()`
"""