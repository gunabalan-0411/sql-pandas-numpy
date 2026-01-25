import pandas as pd

data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})


import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['approved_amount'] = transactions['amount'].where(
        transactions['state'] == 'approved', 0
    )
    transactions['approved_flag'] = (transactions['state'] == 'approved').astype(int)
    
    return (transactions.groupby(
        ['month', 'country'], dropna=False, as_index=False
    ).agg(
        trans_count = ('id','count'),
        approved_count = ('approved_flag', 'sum'),
        trans_total_amount = ('amount', 'sum'),
        approved_total_amount = ('approved_amount', 'sum')
    ))