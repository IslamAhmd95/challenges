#  Problem: Replace Employee ID With The Unique Identifier
#  Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merge_df = employees.merge(employee_uni, on='id', how='left')
    return merge_df[['unique_id', 'name']]





