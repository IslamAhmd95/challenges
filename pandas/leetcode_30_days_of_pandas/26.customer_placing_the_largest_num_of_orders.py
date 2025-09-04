#  Problem: Customer Placing the Largest Number of Orders
#  Link: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].value_counts().reset_index().head(1)[['customer_number']]

# another solution
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby('customer_number')['order_number'].size().reset_index(name='count').sort_values('count', ascending=False).head(1)[['customer_number']]

# another solution
def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby('customer_number')['order_number'].size().reset_index(name='count').nlargest(1, 'count')[['customer_number']]

