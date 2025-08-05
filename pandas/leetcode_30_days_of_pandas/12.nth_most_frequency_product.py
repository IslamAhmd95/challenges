"""
Problem:
    Write a function to find the N-th most frequent product based on the product_name column.

    Return a DataFrame with one column product_name and one row that contains the name of the product with the N-th highest frequency.
    If N is greater than the number of unique product frequencies, return an empty DataFrame.
"""

import pandas as pd

def nth_most_freq_product(products_df: pd.DataFrame, N: int) -> pd.DataFrame:

    grouped_products_df = products_df.groupby('product').count().reset_index()
    grouped_products_df.columns = ['product_name', 'count']
    
    sorted_grouped_products_df = grouped_products_df.sort_values(by=['count', 'product_name'], ascending=[False, True])

    unique_counts = sorted_grouped_products_df['count'].unique()
    
    if N <= 0 or N > len(unique_counts):
        return pd.DataFrame([])

    # Get unique counts only — don't drop full rows based on count.
    nth_count = unique_counts[N-1]

    result = sorted_grouped_products_df[sorted_grouped_products_df['count'] == nth_count]
    
    return result[['product_name']].reset_index(drop=True).head(1)
    # return result[['product_name']].reset_index(drop=True)


products = {
    'product_id': [1, 2, 3, 4, 5, 6, 7],
    'product': ['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'apple']
}

products_df = pd.DataFrame(products)

N = 1
print(nth_most_freq_product(products_df, N))

print("_"*60)

N = 2
print(nth_most_freq_product(products_df, N))

print("_"*60)

N = 3
print(nth_most_freq_product(products_df, N))


"""
Notes:
    1. Get unique counts only — don't drop full rows based on count.
        nth_count = unique_counts[N-1]
"""

print("_"*60)

products = {
    'product_id': [1, 2, 3, 4, 5, 6, 7],
    'product': ['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'apple'],
    'salary': [23, 13, 23, 45, 24, 56, 21]
}

products_df = pd.DataFrame(products)

# sum = products_df.groupby('product')['salary'].sum().to_frame()
# sum.reset_index(inplace=True)
# sum.columns = ['product_name', 'sum_salary']
# print(sum)

products_df['max'] = products_df.groupby('product')['salary'].transform("max")
print(products_df[products_df['max'] == products_df['salary']][['product', 'salary']])