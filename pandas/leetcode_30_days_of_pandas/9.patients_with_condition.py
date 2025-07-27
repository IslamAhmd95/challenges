#  Problem: Patients With a Condition
#  Link: https://leetcode.com/problems/patients-with-a-condition/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# my rate: medium


import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients['conditions'].str.contains(r'(^|\s)DIAB1', regex=True)]




"""
Notes:
    1. (^|\s) = either start of string OR whitespace
    2. (\s|$) = either whitespace OR end of string
    3. str.match() matches only from the beginning of the string
    4. str.contains() which searches anywhere in the string
    5. regex=True tells pandas to interpret the pattern as a regular expression
        df['col'].str.contains('.', regex=True)   # Matches any character
        df['col'].str.contains('.', regex=False)  # Matches only literal dot '.'
"""






