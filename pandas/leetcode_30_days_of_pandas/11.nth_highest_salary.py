#  Problem: Nth Highest Salary
#  Link: https://leetcode.com/problems/nth-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# my rate: medium


import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_employees = employee['salary'].drop_duplicates().sort_values(ascending=False)
    if len(unique_employees) < N or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    return pd.DataFrame({f'getNthHighestSalary({N})': [unique_employees.iloc[N-1]]})




"""
Notes:
    1. unique_salaries.iloc[N - 1] is a scalar (a single value like 200 or None).
        ❌ pd.DataFrame({'salary': 200}) - This will raise an error: "If using all scalar values, you must pass an index"
    2. pd.DataFrame({...}) expects the values in columns to be lists or arrays, not scalars.
        pd.DataFrame({'salary': [200]}) - This creates a DataFrame with one row and one column, which is exactly what we want.
    3. return null is invalid in Python, python uses None, not null.        
"""






