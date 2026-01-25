import pandas as pd
import numpy as np

data = [[1, None], [2, 1], [3, 1], [4, 2], [5, 2]]
tree = pd.DataFrame(data, columns=['id', 'p_id']).astype({'id':'Int64', 'p_id':'Int64'})

'''
Input: 
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
Output: 
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+
'''

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