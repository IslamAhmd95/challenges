import pandas as pd

data = {
    "user_id": [1, 1, 1, 2, 2, 3, 3, 3, 3],
    "bonus":   [10, 5, 8, 20, 15, 7, 3, 6, 6],
    "discount":[2, 1, 3, 5, 2, 1, 1, 2, 1],
    "score":   [80, 90, 85, 70, 75, 88, 92, 85, 90],
    "purchase":[100, 50, 60, 200, 150, 80, 40, 30, 50],
}

df = pd.DataFrame(data)


## transform (broadcasts results back to each row)
df['bonus_share'] = round(df['bonus'] / df.groupby('user_id')['bonus'].transform('sum'), 2)
# print(df)


## Rank or order within groups
df['rank_in_group'] = df.groupby('user_id')['bonus'].rank('dense', ascending=True).astype('int')
# print(df.sort_values(['user_id', 'bonus'], ascending=[True, True]))


## agg with multiple operations
agg_values = df.groupby('user_id').agg(
    avg_bonus = ('bonus', 'mean'),
    max_score = ('score', 'max'),
    total_bonus = ('bonus', 'sum')
)
agg_values = agg_values.reset_index()
agg_values['total_sub_avg'] = round(agg_values['total_bonus'] - agg_values['avg_bonus'], 2)
# print(agg_values)


## Group by multiple columns
df4 = df.groupby(["user_id", "discount"]).agg(
    total_bonus=("bonus", "sum"),
    avg_score=("score", "mean")
)
# print(df4)


df1 = df.groupby('user_id')['bonus'].sum()
df1 = df1.reset_index(name='max_value')
df1 = df1.sort_values(['max_value', 'user_id'], ascending=[False, True]).reset_index(drop=True)
# print(df1)


## apply for custom logic
def custom_calc(group):
    return pd.Series({
        'sum_bonus': group['bonus'].sum(),
        'net_bonus': group['bonus'].sum() - group['discount'].max()
    })

df2 = df.groupby('user_id', as_index=False).apply(custom_calc, include_groups=False)
# print(df2)


## Different aggregations for different columns
df3 = df.groupby('user_id').agg({
    'bonus': ['sum', 'mean'],
    'discount': 'max'
})
# print(df3)
# print(df3['bonus']['sum'].reset_index(name='bonus_sum'))


# --------------------------------------------------------------------------

## The Counting Methods

# size(): counts rows by each group, doesn't care about NaNs.
print(df.groupby('user_id').size().reset_index(name='users_count'))



# count(): counts non-NaNs values per column
print(df.groupby('user_id')['bonus'].count().reset_index(name='bonuses_count'))



# nunique(): Counts unique distinct values in each column (ignores NaNs).
print(df.groupby('user_id')['bonus'].nunique().reset_index(name='bonuses_count'))



# sum(): Normally adds values, but sometimes people use it to “count” booleans (True=1, False=0).
print(df.groupby('user_id', as_index=False)['bonus'].apply(lambda x: (x > 10).sum()).rename(columns={'bonus': 'bonuses_count'}))