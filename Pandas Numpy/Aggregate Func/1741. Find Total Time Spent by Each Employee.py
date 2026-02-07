import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['spent_time'] = employees.out_time - employees.in_time
    return employees.groupby(['emp_id', 'event_day'], as_index=False)['spent_time'].sum().rename(columns={
        "event_day": "day", "spent_time": "total_time"
    })