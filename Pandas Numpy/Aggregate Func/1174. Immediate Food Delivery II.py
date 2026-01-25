import pandas as pd

data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 2, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-12'], [4, 3, '2019-08-24', '2019-08-24'], [5, 3, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13'], [7, 4, '2019-08-09', '2019-08-09']]
delivery = pd.DataFrame(data, columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype({'delivery_id':'Int64', 'customer_id':'Int64', 'order_date':'datetime64[ns]', 'customer_pref_delivery_date':'datetime64[ns]'})


import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    first_order = delivery.groupby(
        'customer_id'
    )[['order_date','customer_pref_delivery_date']].min().reset_index()

    return pd.DataFrame({"immediate_percentage": [round((first_order.order_date == first_order.customer_pref_delivery_date).mean() * 100, 2)]})