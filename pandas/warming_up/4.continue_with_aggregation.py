import pandas as pd

data = {
    "user_id": [1, 1, 1, 2, 2, 3, 3, 3, 3],
    "bonus":   [10, 5, 8, 20, 15, 7, 3, 6, 6],
    "discount":[2, 1, 3, 5, 2, 1, 1, 2, 1],
    "score":   [80, 90, 85, 70, 75, 88, 92, 85, 90],
    "purchase":[100, 50, 60, 200, 150, 80, 40, 30, 50],
}

df = pd.DataFrame(data)


## 1. For each user_id, calculate the total, max bonus and the average score.

# first solution
df1 = df.groupby('user_id').agg(
    total_bonus= ('bonus', 'sum'),
    max_bonus= ('bonus', 'max'),
    avg_score= ('score', 'mean'),
)
# print(df1.reset_index())

# second solution
df1 = df.groupby('user_id').agg({
    'bonus': ['sum', 'max'],
    'score': 'mean'
})
df1.columns = ['_'.join(col) for col in df1.columns.values]
# print(df1.reset_index())



## 2. For each user_id, find the maximum purchase value.
df2 = df.groupby('user_id', as_index=False)['purchase'].max()
# print(df2)



## 3. Add a new column showing each row’s bonus as a percentage of that user’s total bonus.
df['bonus_percentage'] = (df['bonus'] / df.groupby('user_id')['bonus'].sum() * 100).round(2)
print(df)



# 4. For each user_id, compute the net bonus = sum of bonus − sum of discount.
net_bonus = df.groupby('user_id').agg(
    net_bonus=('bonus', 'sum')
) 
net_bonus['net_bonus'] -= df.groupby('user_id')['discount'].sum()
# print(net_bonus)



# 5. For each user_id, rank the rows by purchase (highest purchase gets rank 1).
df['rank'] = df.groupby('user_id')['purchase'].rank('dense', ascending=False)
# print(df)



# 6. For each user_id, return only the top 2 purchases.
print(df.sort_values(['user_id', 'purchase'], ascending=[True, False]).groupby('user_id').head(2))
# or
# print(df.groupby('user_id').apply(lambda grp: grp.nlargest(2, 'purchase')))



# 7. For each user_id, compute (sum of bonus, max score, (sum of bonus − max discount))
g = df.groupby('user_id').agg(
    bonus_sum=('bonus', 'sum'),
    score_max=('score', 'max'),
    max_discount=('discount', 'max')
)
g['final_bonus'] = g['bonus_sum'] - g['max_discount']
df3 = g.drop(columns='max_discount')
print(df3)



# 8. For each user_id, find the average purchase where the score > 85.
print(df[df['score'] > 85].groupby('user_id')['purchase'].mean().round(2).reset_index(name='purchase_avg'))



# 9. For each user_id and discount value, calculate the average score.
df.groupby(['user_id','discount'])['score'].mean().reset_index(name='avg_score')



# 10. Create a new DataFrame showing, for each user_id, the difference between their highest and lowest purchase.
df4 = df.groupby('user_id').apply(lambda grp: grp['purchase'].max() - grp['purchase'].min()
)
# print(df4.reset_index(name='purchase_diff'))