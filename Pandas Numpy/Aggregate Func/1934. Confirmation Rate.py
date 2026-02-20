import pandas as pd
import numpy as np


def confirmation_rate(
    signups: pd.DataFrame, confirmations: pd.DataFrame
) -> pd.DataFrame:
    activity = pd.merge(signups, confirmations, how="left", on="user_id")
    activity["confirmation_rate"] = np.where(activity["action"] == "confirmed", 1, 0)
    return (
        activity.groupby("user_id")["confirmation_rate"].mean().round(2).reset_index()
    )
