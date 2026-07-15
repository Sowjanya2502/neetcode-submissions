-- Write your query below
select customer_id
FROM customers c
WHERE c.revenue>0 AND c.year = 2020;
