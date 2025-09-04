import pandas as pd

data = {
    "user_id": [1, 1, 1, 2, 2, 3, 3, 3, 3],
    "product": ["A", "B", "A", "C", "C", "A", "B", "C", "C"],
    "quantity": [2, 1, 3, 5, 2, 1, 1, 4, 4],
    "price": [10, 20, 10, 15, 15, 10, 20, 15, 15],
    "discount": [0, 5, 0, 0, 5, 0, 0, 5, 0],
}
df = pd.DataFrame(data)


# 1. Unique products per user
# For each user_id, calculate how many unique products they purchased. Then, also add a column that shows the total purchases count.
df1 = df.groupby('user_id', as_index=False).agg(
    unique_products = ('product', 'nunique'),
    total_purchases = ('product', 'size')
)
# print(df1)



# 2. Orders with discount
# For each user_id, count how many rows have discount > 0. (Hint: can be done with sum() since True=1/False=0).
df2 = df[df['discount'] > 0].groupby('user_id').size()
# or
# df2 = df.groupby('user_id').apply(lambda grp: (grp['discount'] > 0).sum(), include_groups=False)

df2 = df2.reset_index(name='discount_count')
# print(df2)



# 3. Product popularity per user
# For each user_id, get the most frequently purchased product (use size or count + logic). Only keep the product name.
df3 = df.groupby(['user_id', 'product'], as_index=False).size().sort_values(['user_id', 'size'], ascending=[True, False]).groupby('user_id').head(1)
print(df3)



# 4. Discounted vs. non-discounted items
# For each user_id, calculate:
    # how many rows had a discount applied (count or sum),
    # how many had no discount,
    # the ratio of discounted to total orders.
grp = df.groupby('user_id')['discount']
df4 = pd.DataFrame({
    'with_discount': grp.apply(lambda x: (x > 0).sum()),
    'no_discount': grp.apply(lambda x: (x == 0).sum())
})
df4['discount_ratio'] = (df4['with_discount'] / (df4['with_discount'] + df4['no_discount'])).round(2)
# print(df4)



# 5. High-spending customers
# For each user_id, compute the total money spent (quantity * price - discount). Then, filter only users who spent more than 60.
df['spent'] = df['quantity'] * df['price'] - df['discount']
total_money = df.groupby('user_id')['spent'].sum().reset_index()
# print(total_money[total_money['spent'] > 60])

# or

# total_money = df.groupby('user_id').apply(lambda grp: ((grp['quantity'] * grp['price']) - grp['discount']).sum(), include_groups=False).reset_index(name='total_spent')
# print(total_money[total_money['total_spent'] > 70])