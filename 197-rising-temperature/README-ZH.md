# Rising Temperature

## Difficulty
Easy

## Question
<p>Given a <code>Weather</code> table, write a SQL query to find all dates&#39; Ids with higher temperature compared to its previous (yesterday&#39;s) dates.</p>

<pre>
+---------+------------------+------------------+
| Id(INT) | RecordDate(DATE) | Temperature(INT) |
+---------+------------------+------------------+
|       1 |       2015-01-01 |               10 |
|       2 |       2015-01-02 |               25 |
|       3 |       2015-01-03 |               20 |
|       4 |       2015-01-04 |               30 |
+---------+------------------+------------------+
</pre>

<p>For example, return the following Ids for the above <code>Weather</code> table:</p>

<pre>
+----+
| Id |
+----+
|  2 |
|  4 |
+----+
</pre>


## Solution
### mysql
```mysql
# Write your MySQL query statement below
SELECT w.Id 
FROM Weather AS w
JOIN Weather AS wj ON DATEDIFF(w.RecordDate, wj.RecordDate) = 1
AND w.Temperature > wj.Temperature
```

## Author
EINDEX