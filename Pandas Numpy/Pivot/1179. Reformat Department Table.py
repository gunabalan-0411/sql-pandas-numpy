import pandas as pd

data = [[1, 8000, 'Jan'], [2, 9000, 'Jan'], [3, 10000, 'Feb'], [1, 7000, 'Feb'], [1, 6000, 'Mar']]
department = pd.DataFrame(data, columns=['id', 'revenue', 'month']).astype({'id':'Int64', 'revenue':'Int64', 'month':'object'})

def reformat_table(department: pd.DataFrame) -> pd.DataFrame:
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    df = department.pivot_table(
        index = 'id',
        columns = 'month',
        values = 'revenue',
        aggfunc = 'sum'
    )
    df = df.reindex(columns = months)
    df.columns = [f'{col}_Revenue' for col in months]
    return df.reset_index()