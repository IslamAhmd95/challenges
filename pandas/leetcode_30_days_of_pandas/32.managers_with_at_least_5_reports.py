#  Problem: Managers with at Least 5 Direct Reports
#  Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    managers = employee.groupby('managerId').agg(
        employees_count = ('id', 'count')
    ).query('employees_count >= 5')
    
    # return employee[employee['id'].isin(managers['managerId'])][['name']]
    return employee.merge(managers, left_on='id', right_on='managerId')[['name']]