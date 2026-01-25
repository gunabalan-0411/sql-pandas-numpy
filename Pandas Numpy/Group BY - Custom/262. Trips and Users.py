import pandas as pd

data = [['1', '1', '10', '1', 'completed', '2013-10-01'], ['2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'], ['3', '3', '12', '6', 'completed', '2013-10-01'], ['4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'], ['5', '1', '10', '1', 'completed', '2013-10-02'], ['6', '2', '11', '6', 'completed', '2013-10-02'], ['7', '3', '12', '6', 'completed', '2013-10-02'], ['8', '2', '12', '12', 'completed', '2013-10-03'], ['9', '3', '10', '12', 'completed', '2013-10-03'], ['10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03']]
trips = pd.DataFrame(data, columns=['id', 'client_id', 'driver_id', 'city_id', 'status', 'request_at']).astype({'id':'Int64', 'client_id':'Int64', 'driver_id':'Int64', 'city_id':'Int64', 'status':'object', 'request_at':'object'})

data = [['1', 'No', 'client'], ['2', 'Yes', 'client'], ['3', 'No', 'client'], ['4', 'No', 'client'], ['10', 'No', 'driver'], ['11', 'No', 'driver'], ['12', 'No', 'driver'], ['13', 'No', 'driver']]
users = pd.DataFrame(data, columns=['users_id', 'banned', 'role']).astype({'users_id':'Int64', 'banned':'object', 'role':'object'})

import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    # Merging banned flags to trips for clients
    trips = pd.merge(trips, users, how = 'left', left_on = 'client_id', right_on = 'users_id')

    # Merging banned flags to trips for drivers
    full_trips = pd.merge(trips, users, how = 'left', left_on = 'driver_id', right_on = 'users_id')

    # Renaming and selecting necessary columns
    full_trips = full_trips.rename(columns={'banned_x':'client_ban', 'banned_y': 'driver_ban'})
    full_trips = full_trips[['id', 'client_id', 'driver_id', 'status', 'request_at', 'client_ban', 'driver_ban']]

    # Filtering data
    filtered_trips = full_trips[
        (full_trips.client_ban == 'No') &
        (full_trips.driver_ban == 'No') &
        (full_trips.request_at.between('2013-10-01', '2013-10-03'))
    ]
    
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