#  Problem: Group Sold Products By The Date
#  Link: https://leetcode.com/problems/group-sold-products-by-the-date/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return activities.groupby('sell_date', as_index=False)['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))
    ])
    

# another solution
def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grp = activities.sort_values(['sell_date', 'product']).groupby('sell_date')['product']
    activities_cats = grp.nunique().reset_index(name='num_sold')
    activities_cats['products'] = grp.agg(lambda x: ','.join(x.unique())).reset_index(name='products')['products']
    return activities_cats




