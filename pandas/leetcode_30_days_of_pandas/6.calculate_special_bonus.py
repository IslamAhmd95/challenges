#  Problem: Calculate Special Bonus
#  Link: https://leetcode.com/problems/calculate-special-bonus/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# my rate: medium


import pandas as pd
import numpy as np   # pyright: ignore[reportMissingImports]

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (~employees['name'].str.startswith('M')) & (employees['employee_id'] % 2 != 0)
    
    employees['bonus'] = employees['salary'].where(condition, 0)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')


# another solution
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (~employees['name'].str.startswith('M')) & (employees['employee_id'] % 2 != 0)
    employees['bonus'] = np.where(condition, employees['salary'], 0)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')


# another solution
def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    def bonus_condition(row):
        if not row['name'].startswith('M') and row['employee_id'] % 2 != 0:
            return row['salary']
        return 0
    employees['bonus'] = employees.apply(bonus_condition, axis=1)
    return employees[['employee_id', 'bonus']].sort_values(by='employee_id')



"""
Notes:
    1. axis=1 → apply to each row (horizontally).
    2. 
    | Type                | Input to function      | axis=  | Description            |
    | ------------------- | ---------------------- | ------ | ---------------------- |
    | `DataFrame.apply()` | Row (Series) or Column | 1 or 0 | Apply on row or column |
    | `Series.apply()`    | Single value (cell)    | –      | Apply on each cell     |

    3. np.where(condition, value_if_true, value_if_false) - works with Pandas Series or NumPy arrays.
    4. Series.where(condition, other) - Keeps values where condition is True, and replaces others with other.

"""


