#  Problem: Delete Duplicate Emails
#  Link: https://leetcode.com/problems/delete-duplicate-emails/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset=['email'], keep='first', inplace=True)  
    # person.drop_duplicates('email', inplace=True)



"""
Notes:
    1. Using `subset='email'` and `keep='first'` makes the intent clearer, 
       which is better for interviews, collaboration, and code readability —
       even though the function works without them due to default behavior.
       
    2. The function does not return a new DataFrame — it modifies the `person` DataFrame in place.
"""






