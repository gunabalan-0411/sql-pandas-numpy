# MySQL

## JOIN
* Keep the table left and use left join where you want to keep the category even if there is no records from right

## Window Function
SUM function with over
```sql
  SELECT
      person_name,
      SUM(weight) OVER (ORDER BY turn) AS weight_sofar
  FROM Queue
```
## Agg
  Conditional aggregations
  ```sql
  SELECT
    DATE_FORMAT(trans_date, "%Y-%m") AS month,
    country,
    COUNT(trans_date) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN AMOUNT ELSE 0 END) AS approved_total_amount
  FROM
    Transactions
  GROUP BY DATE_FORMAT(trans_date, "%Y-%m"), country
  ```

## Date
  DATE_FORMAT(col_name, "%Y-%m")
  
## Update
  - UPDATE Salary SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END
    
## Data Type
  - CAST(COLUMN_NAME AS Dat-type)
  - Data-type: UNSIGNED, SIGNED

## Date
  -	DATE_ADD('date', INTERVAL Num DAY)
  -	Use BETWEEN for date range (BETWEEN '' AND '')
  - DATE_FORMAT(col, '%m-%Y') #02-2026

## Math
  - Division	we can directly divide num of rows from table by a calculated value from another table by 2 select statement

## JOIN
  - you can filter while join, (just add condition without adding WHERE, after on matching terms)

## Generate Truth values for aggregation function
``` sql
SELECT ROUND(AVG(immediate_order) * 100, 2) AS immediate_percentage FROM
(
SELECT MIN(order_date) = MIN(customer_pref_delivery_date) AS immediate_order FROM Delivery GROUP BY customer_id
) as lookup
```
## REGEXP

``` sql
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$';
'(^| )word' -- means any word that starts with string a space before it
```

## String

```sql
SUBSTR(col_name, start, end)

```
