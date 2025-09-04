"""
Problem:
    find the number of unique customers who have at least one amount strictly greater than 500.
"""

import pandas as pd

store = pd.DataFrame({
    'bill_id': [6, 8, 4, 11, 13],
    'customer_id': [1, 1, 2, 3, 3],
    'amount': [549, 834, 394, 657, 257]
})

print(store.loc[store['amount'] > 500, 'customer_id'].nunique())



"""
Notes:
    1. .nunique() → counts unique values for each column in the filtered rows.
"""