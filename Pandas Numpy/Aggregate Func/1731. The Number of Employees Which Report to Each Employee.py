import pandas as pd
import numpy as np

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    round_off = lambda x: round(x+.00001, 0)
    employees = employees.merge(employees, left_on='employee_id', right_on='reports_to')
    managers = employees.groupby('employee_id_x', as_index=False).agg(
        name = ('name_x', 'max'),
        reports_count = ('employee_id_y', 'count'),
        average_age = ('age_y', 'mean')
    ).rename(columns={'employee_id_x': 'employee_id'})
    managers['average_age'] = managers.average_age.apply(round_off)
    managers = managers.sort_values('employee_id')
    return managers