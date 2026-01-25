import pandas as pd

data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype({'sale_id':'Int64', 'product_id':'Int64', 'year':'Int64', 'quantity':'Int64', 'price':'Int64'})

def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    first_year = sales.groupby('product_id')['year'].min().rename('first_year').reset_index()
    result =  pd.merge(
        sales, 
        first_year,
        how = 'left',
        on = 'product_id'
    )

    return result[result['year'] == result['first_year']][['product_id', 'first_year', 'quantity', 'price']]
