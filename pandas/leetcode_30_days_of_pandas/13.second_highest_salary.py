#  Problem: Second Highest Salary
#  Link: https://leetcode.com/problems/nth-highest-salary/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# my rate: medium


import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].drop_duplicates()
    second_highest = unique_salaries.nlargest(2).iloc[-1] if len(unique_salaries) >= 2 else None

    return pd.DataFrame({'SecondHighestSalary': [second_highest]})


# another solution
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee['salary'].rank(method='dense', ascending=False)
    second = employee[employee['rank'] == 2]
    return pd.DataFrame({'SecondHighestSalary': [None if len(second) == 0 else second.iloc[0]['salary']]})


# another solution
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_sorted_salaries = employee.drop_duplicates('salary').sort_values('salary', ascending=False)
    if len(unique_sorted_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    return pd.DataFrame({'SecondHighestSalary': [unique_sorted_salaries.iloc[1]['salary']]})




"""
Notes:
    1. nlargest(n) and nsmallest(n):

        - These are Pandas methods used to get the top n largest or smallest values from a Series or DataFrame.
        - They are faster and more efficient than using .sort_values() + .head(n) or .tail(n), especially on large datasets.
            - Example:
                df['salary'].nlargest(2)  # returns the top 2 highest salaries

    2. rank(method='dense'):

        - Similar to the RANK() function in SQL when using DENSE_RANK().
        - It assigns consecutive ranks without skipping numbers for ties.
        - Example: if salaries are [5000, 4000, 4000, 3000], the ranks would be [1, 2, 2, 3].
        - Used to find the 2nd highest salary by filtering rows where rank = 2.

    3. iloc[-1]:

        - This is exactly like using list indexing:
                iloc[-1] → last item.
                iloc[-2] → second to last.
                iloc[1] → second item (0-based indexing).
        - So in this case:
            nlargest(2) returns the top 2 salaries in descending order.
            iloc[-1] gets the second one, which is the second highest salary.
"""






