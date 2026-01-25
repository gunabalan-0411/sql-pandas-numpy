import pandas as pd

data = [[1, "Avengers"], [2, "Frozen 2"], [3, "Joker"]]
movies = pd.DataFrame(data, columns=["movie_id", "title"]).astype(
    {"movie_id": "Int64", "title": "object"}
)
data = [[1, "Daniel"], [2, "Monica"], [3, "Maria"], [4, "James"]]
users = pd.DataFrame(data, columns=["user_id", "name"]).astype(
    {"user_id": "Int64", "name": "object"}
)
data = [
    [1, 1, 3, "2020-01-12"],
    [1, 2, 4, "2020-02-11"],
    [1, 3, 2, "2020-02-12"],
    [1, 4, 1, "2020-01-01"],
    [2, 1, 5, "2020-02-17"],
    [2, 2, 2, "2020-02-01"],
    [2, 3, 2, "2020-03-01"],
    [3, 1, 3, "2020-02-22"],
    [3, 2, 4, "2020-02-25"],
]
movie_rating = pd.DataFrame(
    data, columns=["movie_id", "user_id", "rating", "created_at"]
).astype(
    {
        "movie_id": "Int64",
        "user_id": "Int64",
        "rating": "Int64",
        "created_at": "datetime64[ns]",
    }
)


def movie_rating(  # noqa: F811
    movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame
) -> pd.DataFrame:
    user_rating = pd.merge(movie_rating, users, how="left", on="user_id")
    title_rating = pd.merge(movie_rating, movies, how="left", on="movie_id")

    highest_rated_user = (
        user_rating.groupby("name", as_index=False)["rating"]
        .count()
        .sort_values(["rating", "name"], ascending=[False, True])
        .head(1)["name"]
        .values[0]
    )
    title_rating = title_rating[
        (title_rating.created_at.dt.year == 2020)
        & (title_rating.created_at.dt.month == 2)
    ]
    highest_average_title = (
        title_rating.groupby("title", as_index=False)["rating"]
        .mean()
        .sort_values(["rating", "title"], ascending=[False, True])
        .head(1)["title"]
        .values[0]
    )

    return pd.DataFrame({"results": [highest_rated_user, highest_average_title]})
