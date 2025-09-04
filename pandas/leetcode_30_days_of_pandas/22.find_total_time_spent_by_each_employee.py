#  Problem: Find Total Time Spent by Each Employee
#  Link: https://leetcode.com/problems/find-total-time-spent-by-each-employee/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    return employees.groupby(['event_day', 'emp_id'], as_index= False)['total_time'].sum().rename(columns={'event_day': 'day'})


# another solution
def custom_calc(group):
    return pd.Series({
        'total_time': group['out_time'].sum() - group['in_time'].sum()
    })

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    total_df = employees.groupby(['event_day', 'emp_id'], as_index=False).apply(custom_calc)
    total_df.rename(columns={'event_day': 'day'}, inplace=True)
    return total_df




"""
Notes:

    1. `as_index=False` means event_day and emp_id will stay as columns instead of becoming index, it's similar to using `reset_index()`
"""