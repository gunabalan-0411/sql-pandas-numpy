import pandas as pd
import numpy as np

data = [[8], [8], [3], [3], [1], [4], [5], [6]]
my_numbers = pd.DataFrame(data, columns=['num']).astype({'num':'Int64'})

import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    
    return pd.DataFrame({
        "num": [my_numbers.drop_duplicates(keep=False)['num'].max()]
    })
