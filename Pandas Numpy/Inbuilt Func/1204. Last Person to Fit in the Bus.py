import pandas as pd

data = [[5, 'Alice', 250, 1], [4, 'Bob', 175, 5], [3, 'Alex', 350, 2], [6, 'John Cena', 400, 3], [1, 'Winston', 500, 6], [2, 'Marie', 200, 4]]
queue = pd.DataFrame(data, columns=['person_id', 'person_name', 'weight', 'turn']).astype({'person_id':'Int64', 'person_name':'object', 'weight':'Int64', 'turn':'Int64'})

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue = queue.sort_values('turn', ascending=True)
    queue['tot_weight'] = queue['weight'].cumsum()
    return queue[queue.tot_weight <= 1000][['person_name']].tail(1).reset_index(drop=True)