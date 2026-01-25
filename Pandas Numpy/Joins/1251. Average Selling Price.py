import pandas as pd
import numpy as np

data = [
    [1, "2019-02-17", "2019-02-28", 5],
    [1, "2019-03-01", "2019-03-22", 20],
    [2, "2019-02-01", "2019-02-20", 15],
    [2, "2019-02-21", "2019-03-31", 30],
]
prices = pd.DataFrame(
    data, columns=["product_id", "start_date", "end_date", "price"]
).astype(
    {
        "product_id": "Int64",
        "start_date": "datetime64[ns]",
        "end_date": "datetime64[ns]",
        "price": "Int64",
    }
)
data = [
    [1, "2019-02-25", 100],
    [1, "2019-03-01", 15],
    [2, "2019-02-10", 200],
    [2, "2019-03-22", 30],
]
units_sold = pd.DataFrame(
    data, columns=["product_id", "purchase_date", "units"]
).astype({"product_id": "Int64", "purchase_date": "datetime64[ns]", "units": "Int64"})


def average_selling_price(
    prices: pd.DataFrame, units_sold: pd.DataFrame
) -> pd.DataFrame:
    sales = pd.merge(prices, units_sold, how="left", on="product_id")
    sales = sales[
        sales.purchase_date.isna()
        | sales["purchase_date"].between(sales.start_date, sales.end_date)
    ]
    sales["overall_price"] = sales["price"] * sales["units"]
    sales = sales.groupby("product_id", as_index=False).agg(
        total_price_sum=("overall_price", "sum"), total_units=("units", "sum")
    )
    sales["average_price"] = (sales.total_price_sum / sales.total_units).round(2)
    sales["average_price"] = np.where(
        sales["total_units"] > 0,
        (sales["total_price_sum"] / sales["total_units"]).round(2),
        0,
    )
    return sales[["product_id", "average_price"]]
