#  Problem: Big Countries
#  Link: https://leetcode.com/problems/big-countries/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world[(world['area'] >= 3000000) | (world['population'] >= 25000000)][['name', 'population', 'area']]


"""
Notes:
    1. "Series" -> one bracket 
        world['name']
    2. "DataFrame" -> double brackets  
        world[['name']] , world[['name', 'area', 'population']]
"""