/*
Create table If Not Exists Tree (id int, p_id int)
Truncate table Tree
insert into Tree (id, p_id) values ('1', NULL)
insert into Tree (id, p_id) values ('2', '1')
insert into Tree (id, p_id) values ('3', '1')
insert into Tree (id, p_id) values ('4', '2')
insert into Tree (id, p_id) values ('5', '2')

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
*/

SELECT
    id,
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        -- marking id as leaf who aren't a parent
        WHEN id NOT IN (
            SELECT DISTINCT CAST(p_id AS UNSIGNED) FROM Tree WHERE p_id IS NOT NULL
        ) THEN 'Leaf'
        ELSE 'Inner'
    END AS type
FROM
    Tree