#  Problem: Customers Who Never Order
#  Link: https://leetcode.com/problems/customers-who-never-order/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# my rate: medium


import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    mask = ~customers['id'].isin(orders['customerId'])
    return customers.loc[mask, ['name']].rename(columns={'name': 'Customers'})


# another solution using merge
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    filtered = merged_df[merged_df['id_y'].isnull()][['name']]
    filtered.columns = ['Customers']
    return filtered



"""
Notes:
    1. ~ means "not"
    2. This mask is a Boolean Series. It aligns with the rows of the customers DataFrame — one True or False per row.
    3. We give .loc a Boolean Series (same length as the DataFrame). It will keep only the rows where the value is True, and returns only name ['name']
    4. mask (variable) is a common convention, usually refers to a Boolean filter — like [True, False, True, False]
    5. mask() (method): Pandas function used to replace values where a condition is True.
        df = pd.DataFrame({'score': [90, 60, 30]})
        df.mask(df['score'] < 50, 0)  # replace any value that is smaller than 50 with 0
    6. rename() is used only for changing column names (or index names).
        df.rename(columns={"old": "new"})
        df.rename(index={0: "first"})
"""


# similar problem 
# returns the names of products never sold — i.e., whose IDs are not in orders.productId. Name the output column as Products.


products = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["TV", "Laptop", "Phone", "Headphones"]
})

orders = pd.DataFrame({
    "id": [101, 102, 103],
    "product_id": [2, 3, 3]
})


mask = ~products['id'].isin(orders['product_id'])
print(products.loc[mask, ['name']].rename(columns={'name': 'Products'})) 