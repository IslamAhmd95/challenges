#  Problem: Department Highest Salary
#  Link: https://leetcode.com/problems/department-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# my rate: medium


import pandas as pd


def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merge = employee.merge(department, left_on='departmentId', right_on='id')
    merge['max'] = merge.groupby('departmentId')['salary'].transform('max')
    result = merge[merge['salary'] == merge['max']][['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    return result

# another solution
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['salary_rank'] = employee.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    top_employees = employee[employee['salary_rank'] == 1]
    merged = pd.merge(top_employees, department, left_on='departmentId', right_on='id')
    result = merged[['name_y', 'name_x', 'salary']]
    result.columns = ['Department', 'Employee', 'Salary']
    return result


"""
Notes:
    1. transform() in pandas is conceptually similar to window functions in SQL., transform('max') returns the max salary repeated for each row in its group — unlike agg() or apply() which reduce the rows.
"""






