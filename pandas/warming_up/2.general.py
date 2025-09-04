import pandas as pd
import numpy as np  # pyright: ignore[reportMissingImports]


employees = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "department": ["HR", "IT", "Finance", "IT", "HR"]
})

salaries = pd.DataFrame({
    "emp_id": [1, 2, 3, 5],
    "salary": [50000, 60000, 75000, 62000]
})


# 1. Merge employees and salaries on id / emp_id to create one DataFrame.
df = pd.merge(employees, salaries, left_on='id', right_on='emp_id', how='inner')
print(df)


# 2. After merging, find the average salary per department.
print(df.groupby('department')['salary'].mean())


# 3. Find employees who don’t have a salary record.
mask = ~employees['id'].isin(salaries['emp_id'])
print(employees.loc[mask])
# or
df1 = pd.merge(employees, salaries, left_on='id', right_on='emp_id', how='left')
print(df1[df1['emp_id'].isna()][['id', 'name', 'department']])


# 4. Add a column "high_earner" that is "Yes" if salary > 60000, else "No".
df1['high_earner'] = np.where(df1['salary'] > 60000, 'Yes', 'No')
print(df1)


# 5. Show the top 2 highest-paid employees in the IT department.
print(df1[df1['department'] == 'IT'].nlargest(2, 'salary'))


# 6. Count how many employees are in each department and include those without salaries.
df2 = df1.groupby('department')['id'].count().reset_index()  # using id since it's a non-null column
print(df2)


# 7. Use .agg() to calculate both the average and maximum salary per department.
print(df.groupby('department')['salary'].agg(['mean', 'max']))


# 8. Create a pivot table with department as index and high_earner as columns, counting employees.
pivot = df1.pivot_table(index='department', values='id', columns='high_earner', aggfunc='count')   # values='id' → what to count in each group (any non-null column works).
print(pivot)


# 9. Write a custom function that categorizes age groups (<30: Young, 30–40: Mid, >40: Senior) and apply it to a new column "age_group". (You’ll need to add an "age" column to employees first — feel free to make one up, e.g. [23,34,45,28,40].)
def categorize_age(age):
    if age < 30:
        return 'Young'
    elif age >= 30 and age <= 40:
        return 'Mid'
    elif age > 40:
        return 'Senior'

df1['age'] = [23,34,45,28,40]
df1['age_group'] = df1['age'].map(categorize_age)
# df1['age_group'] = df1['age'].apply(categorize_age)
print(df1)


# 10. Rank all employees by salary (highest salary gets rank 1).
df1['rank'] = df1['salary'].rank(method='max', ascending=False).fillna(0).astype(int)
print(df1)




"""
Notes:
    1. nlargest() and nsmallest():
        - These methods are efficient for directly getting the top or bottom N values based on a specific column
            df1.nlargest(2, 'salary')   # returns a df
            df['salary].nlargest(2)     # returns a series
"""