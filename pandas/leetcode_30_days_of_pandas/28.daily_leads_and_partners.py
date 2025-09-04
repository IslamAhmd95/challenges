#  Problem: Daily Leads and Partners
#  Link: https://leetcode.com/problems/daily-leads-and-partners/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(['date_id', 'make_name'], as_index=False).agg(
        unique_leads = ('lead_id', 'nunique'),
        unique_partners = ('partner_id', 'nunique'),
    )

# another solution
def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return daily_sales.groupby(['date_id', 'make_name'], as_index=False).nunique().rename(columns={'lead_id': 'unique_leads', 'partner_id': 'unique_partners'})





