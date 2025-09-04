"""
Problem:
    The task is to compute the percentage of immediate orders in the entire table.

    An order counts as immediate when the order_date is exactly equal to the customer_pref_delivery_date, otherwise it's scheduled.
"""


import pandas as pd

orders = pd.DataFrame({
    "delivery_id": [1, 2, 3, 4, 5],
    "customer_id": [1, 2, 1, 3, 4],
    "order_date": ["2019-01-01", "2019-01-01", "2019-01-02", "2019-01-02", "2019-01-03"],
    "customer_pref_delivery_date": ["2019-01-01", "2019-01-02", "2019-01-02", "2019-01-05", "2019-01-03"],
    "delivery_date": ["2019-01-01", "2019-01-02", "2019-01-02", "2019-01-06", "2019-01-03"]
})


total_orders = len(orders)
immediate_orders = len(orders[orders['order_date'] == orders['customer_pref_delivery_date']])
result = round((immediate_orders / total_orders) * 100, 2)
print(result)
