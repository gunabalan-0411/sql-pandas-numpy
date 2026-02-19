import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    sal_slabs = ["Low Salary", "Average Salary", "High Salary"]
    desired_order = ["High Salary", "Low Salary", "Average Salary"]
    accounts["category"] = pd.cut(
        accounts["income"],
        bins=[float("-inf"), 20000 - 1, 50000, float("inf")],
        labels=sal_slabs,
        right=True,
    )
    accounts = (
        accounts.groupby("category")["account_id"]
        .count()
        .reindex(desired_order, fill_value=0)
        .reset_index()
        .rename(columns={"account_id": "accounts_count"})
    )
    return accounts
