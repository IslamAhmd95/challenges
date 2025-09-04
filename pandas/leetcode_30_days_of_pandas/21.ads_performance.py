"""
Problem:
    Calculate the Click-Through Rate (CTR) for each ad using this formula:

        If (clicks + views) = 0, then CTR = 0.00.

        Otherwise:

        CTR =
        ( number of ’Clicked’ / (number of ’Clicked’ + number of ’Viewed’) ) × 100

    Round the result to two decimal places.
"""


import pandas as pd


def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    counts = pd.crosstab(ads['ad_id'], ads['action'])
    counts = counts.reindex(columns=['Clicked', 'Viewed'], fill_value=0)

    clicks = counts['Clicked']
    views = counts['Viewed']

    ctr = (clicks / (clicks + views)) * 100
    ctr = ctr.fillna(0).round(2)

    result = ctr.reset_index(name='ctr')
    result = result.sort_values(['ctr', 'ad_id'], ascending=[False, True]).reset_index(drop=True)

    return result



ads = pd.DataFrame({
    "ad_id":   [1, 2, 3, 5, 1, 2, 3, 1, 2, 1],
    "user_id": [1, 2, 3, 5, 7, 7, 5, 4, 11, 2],
    "action":  ["Clicked", "Clicked", "Viewed", "Ignored", 
                "Ignored", "Viewed", "Clicked", "Viewed", 
                "Viewed", "Clicked"]
})



print(ads_performance(ads))


"""
Notes:

    1. counts.reindex(columns=['Clicked', 'Viewed'], fill_value=0)

        - counts is a DataFrame that came from a pivot table (or groupby().size().unstack()), so it has columns like Clicked, Viewed.

        - The .reindex(columns=[...]) explicitly tells pandas:
            "I only want these columns in this exact order."
            Even if a category didn’t exist in the original data (e.g., no rows where action = 'Clicked'), .reindex ensures the column is there.

        - fill_value=0 means:
            If a column doesn’t exist or has missing values (NaN), replace them with 0.
            👉 If you already had both Clicked and Viewed columns, then fill_value=0 doesn’t visibly change anything — that’s why you didn’t notice a difference.
            But it’s there as a safety net.

    2. ctr.reset_index(name='ctr')

        - Before this, ctr is probably a Series (like user_id as the index, CTR values as the Series data).

        - .reset_index() moves the index (user_id) back into a normal column.

        - name='ctr' tells pandas: "Name the Series column 'ctr' instead of leaving it unnamed."
"""