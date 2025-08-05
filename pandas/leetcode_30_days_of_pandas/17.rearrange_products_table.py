#  Problem: Rearrange Products Table
#  Link: https://leetcode.com/problems/rearrange-products-table/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    return  pd.melt(products, 
                id_vars='product_id',
                value_vars=['store1', 'store2', 'store3'], 
                var_name='store', 
                value_name='price'    
            ).dropna()

# second solution
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    store1 = products[~products['store1'].isnull()][['product_id', 'store1']].rename(columns={'store1': 'price'})
    store1['store'] = 'store1'

    store2 = products[~products['store2'].isnull()][['product_id', 'store2']].rename(columns={'store2': 'price'})
    store2['store'] = 'store2'

    store3 = products[~products['store3'].isnull()][['product_id', 'store3']].rename(columns={'store3': 'price'})
    store3['store'] = 'store3'
    result = pd.concat([store1, store2, store3])
    return result



"""
Notes:

    1. What is Unpivoting?
        - **Unpivoting**: The process of converting **columns into rows**.
        - Example: Converting a wide table where each store has its own column into a long format with a single `store` column.
        - In **Pandas**, this is done using `DataFrame.melt()`.

    2. What is Pivoting?
        - **Pivoting**: The opposite of unpivoting — converting **rows into columns**.
        - In **Pandas**, this is done using `DataFrame.pivot()` or `pivot_table()`.

    3. Use `pd.melt` to convert wide tables into long format by unpivoting columns.
        - id_vars: columns to keep as identifiers (product_id)
        - value_vars: columns to unpivot (store1, store2, store3)
        - var_name: name of the new column for former column names (store)
        - value_name: name of the new column for values (price)
        - dropna(): removes rows with missing prices
       
    4. pd.concat([...]) stacks multiple DataFrames vertically (row-wise).
"""