import pandas as pd

data = [
    [1, "Winston", "winston@leetcode.com"],
    [2, "Jonathan", "jonathanisgreat"],
    [3, "Annabelle", "bella-@leetcode.com"],
    [4, "Sally", "sally.come@leetcode.com"],
    [5, "Marwan", "quarz#2020@leetcode.com"],
    [6, "David", "david69@gmail.com"],
    [7, "Shapiro", ".shapo@leetcode.com"],
]
users = pd.DataFrame(data, columns=["user_id", "name", "mail"]).astype(
    {"user_id": "int64", "name": "object", "mail": "object"}
)


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = "^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$"
    return users[users.mail.str.match(pattern, na=False)]
