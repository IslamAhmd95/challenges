#  Problem: Recyclable and Low Fat Products
#  Link: https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[
        (products['low_fats'] == 'Y') &
        (products['recyclable'] == 'Y')
        ][['product_id']]

