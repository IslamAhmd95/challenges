#  Problem: Find Users With Valid E-Mails
#  Link: https://leetcode.com/problems/find-users-with-valid-e-mails/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata
# my rate: medium


import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.match(r'^[a-zA-Z][a-zA-Z0-9\-_.]*@leetcode\.com$')]


"""
Notes:
    ^[a-zA-Z]             # starts with a letter
    [a-zA-Z0-9_.-]*       # followed by letters, digits, underscore, dot, or dash (0 or more)
    @leetcode\.com        # must end with @leetcode.com
    \.                    # A dot . in regex means “any character”, so we escape it with \. to mean a literal dot (.)
    .                     # Match any single character except newline (\n) , a.b = avb or a9b or a!b or a%b ,  ... means any 3 characters like abc, 123, -+@, x.y, etc.
    $                     # no extra characters after .com
    \-                    # - (dash) inside brackets means range "a-z", so we have to escape it also or place it at the end
"""






