#  Problem: Article Views I
#  Link: https://leetcode.com/problems/article-views-i/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors = views[views['author_id'] == views['viewer_id']][['author_id']]
    return authors.rename(columns={'author_id': 'id'}).drop_duplicates().sort_values(by='id')


# another solution
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'id':
        sorted(views.loc[views['author_id'] == views['viewer_id']]['author_id'].unique())
    })



"""
Notes:
    1. unique() works with series
    2. drop_duplicates() works with dataframes, no parameters means unique rows based on all columns (default behavior)
    3. df.drop_duplicates(subset=['name', 'age']) means drop duplicates on columns name, age
    4. views['author_id'] == views['viewer_id'] → gives you a Boolean Series (True/False for each row).
    5. views.loc[...] or views[...] → use that Boolean Series to filter rows.
"""