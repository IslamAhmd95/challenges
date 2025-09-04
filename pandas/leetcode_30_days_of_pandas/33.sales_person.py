#  Problem: Sales Person
#  Link: https://leetcode.com/problems/sales-person/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata



import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    orders_companies = pd.merge(company[['com_id', 'name']], orders[['com_id', 'sales_id']], on='com_id')
    RED_orders = orders_companies[orders_companies['name'] == 'RED']
    result = sales_person[['sales_id', 'name']].merge(RED_orders, how='left', on='sales_id')
    return result[result['com_id'].isnull()][['name_x']].rename(columns={'name_x': 'name'})
