import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [23, 34, 45, 28, 40],
    "department": ["HR", "IT", "Finance", "IT", "HR"],
    "salary": [50000, 60000, 75000, 55000, 62000]
}

df = pd.DataFrame(data)

# 1. Select the name column as a Series.
print(df['name'])


# 2. Select only the name and age columns as a DataFrame.
print(df[['name', 'age']])


# 3. Get the first 3 rows of the DataFrame.
print(df.head(3))
print(df.loc[0:2])


# 4. Select the row where id = 3.
print(df[df['id'] == 3])


# 5. Filter all employees older than 30.
print(df.loc[df['age'] > 30])


# 6. Filter employees from the IT department.
print(df[df['department'] == 'IT'])


# 7. Get the average salary of all employees.
print(df['salary'].mean())


# 8. Get the maximum age in the DataFrame.
print(df['age'].max())


# 9. Sort the DataFrame by age in descending order.
print(df.sort_values(by='age', ascending=False))


# 10. Count how many employees are in each department.
print(df.groupby('department').size())
# print(df.groupby('department').value_counts())


# 11. Select only the name and department columns for employees older than 30.
print(df.loc[df['age'] > 30, ['name', 'department']])
# print(df[df['age'] > 30][['name', 'department']])


# 12. Find the average salary per department.
print(df.groupby('department')['salary'].mean())


# 13. Find the employee with the highest salary.
print(df.loc[df['salary'].idxmax()])
# print(df[df['salary'] == df['salary'].max()])


# 14. Add a new column "seniority" where employees older than 35 are "Senior" and the rest "Junior".
df['seniority'] = df['age'].apply(lambda x: 'Senior' if x > 35 else 'Junior')
print(df)


# 15. Rename the column "salary" to "income".
df.rename(columns={'salary': 'income'}, inplace=True)
print(df)


# 16. Show only employees whose names start with "A".
print(df[df['name'].str.startswith('A')])
# print(df[df['name'].str.contains("^A")])


# 17. Sort employees first by department (ascending) then by income (descending).
print(df.sort_values(by=['department', 'income'], ascending=[True, False]))


# 18. Calculate the total salary of employees in IT.
print(df.groupby('department')['income'].sum().loc['IT'])
# print(df[df['department'] == 'IT']['income'].sum())


# 19. Create a new DataFrame with only HR department employees.
df1 = df[df['department'] == 'HR']
print(df1)


# 20. Find how many employees are "Senior" vs "Junior" (from problem 14).
print(df.groupby('seniority').size())
# print(df.groupby('seniority').value_counts())





"""
Notes:
    1. .count() → counts non-null values per column - exercise 10.
    2. .loc[rows, cols] → clean way to filter both at once.
    3. idxmax() → quick way to find row with max value.
    4. np.where → often faster than .apply for conditional columns.
        import numpy as np
        df['seniority'] = np.where(df['age'] > 35, 'Senior', 'Junior')

    5. value_counts() → easy way to count categories.
"""