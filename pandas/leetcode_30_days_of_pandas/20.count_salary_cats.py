#  Problem: Count Salary Categories
#  Link: https://leetcode.com/problems/count-salary-categories/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd


def income_cat(income):
    if income < 20000:
        return "Low Salary"
    elif income >= 20000 and income <= 50000:
        return "Average Salary"
    elif income > 50000:
        return "High Salary"


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    cats = ["Low Salary", "Average Salary", "High Salary"]
    accounts['category'] = accounts['income'].apply(income_cat)
    counts_df = accounts.groupby('category').size().reindex(cats, fill_value=0).reset_index(name="accounts_count")
    return counts_df


# another solution
def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'category': ["Low Salary", "Average Salary", "High Salary"],
        'accounts_count': [
            accounts[accounts.income < 20000].shape[0],
            accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)].shape[0],
            accounts[accounts.income > 50000].shape[0]
        ]
    })