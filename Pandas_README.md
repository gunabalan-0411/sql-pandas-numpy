# Pandas

## Inbuilt

```python
queue['weight_so_far'] = queue['weight'].cumsum()
```

## Grouping

### Group By Function using agg (efficient)
we can also use lambda x: func(x) for custom aggregation function
```python
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
```

### Group By Function using apply (inefficient)

* Use apply for custom group by calculation for better code readability
* Return pd.Series
* you can also use filtered data inside it
* before returning the result handle the edge cases like empty df or get back the groupby column name

```python
    # Calculating: Cancellation Rate
    result = filtered_trips.groupby('request_at').apply(
        lambda group: pd.Series(
            {
                "Cancellation Rate": round(
                    (group['status'] != 'completed').sum()/ len(group), 2
                )
            }
        )
    )
    if result.empty:
        return pd.DataFrame(columns=['Day', 'Cancellation Rate'])
    result.index.name = None
    return result.reset_index().rename(columns= {'index': 'Day'})
```

### Group By Range Condition

```python
df['age_group'] = pd.cut(
    df['age'],
    bins=[0, 18, 30, 50, 100],
    labels=['Teen', 'Young Adult', 'Adult', 'Senior']
)
```

## Vectorized Mapping
``` python
# Solution
def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # Writing vectorized condition
    root_condtion = tree['p_id'].isna()
    inner_condition = tree['id'].isin(
        tree['p_id'].dropna().unique()
    )
    leaf_condition = ~root_condtion & ~inner_condition
    # mapping condition to labels
    tree['type'] = np.select(
        (root_condtion, inner_condition, leaf_condition),
        ['Root', 'Inner', 'Leaf']
    )
    return tree[['id', 'type']]
```

## Merging

code to rename column while grouping
```python
.min().rename('first_year').reset_index()
```

## Pivot

code to rename column while grouping
```python
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
```

## Regex
For matching whole string by pattern and say its True or False
col.str.match(patter, na=False)
- ' ^ ' - starts with
- ' * ' - 0 or more
- ' \. ' - saying . is char not syntax
- ' $ ' - ends with

```python
pattern = "^[A-Za-z][A-Za-z0-9._-]*@leetcode\.com$"

```
For searching word in whole text say its True or False
col.str.contains(pattern, regex=True, na=False)

```python
'(^| )DIAB1' # search for a word starting with DIAB1
```

## Date
Date filter

```python
# df.date_col.dt.year, month etc
```

## Math Misc
* Round off
* floating-point precision artifact
* We add a small epsilon before rounding to avoid floating-point precision errors that can incorrectly round values like 30.499999 instead of 30.5. This ensures consistent, business-expected rounding behavior.
```python
round_off = lambda x: round(x+.00001, 0)
managers['average_age'] = managers.average_age.apply(round_off)

```

## Data Science

```python
print(df.dtypes == 'object')
categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

```
