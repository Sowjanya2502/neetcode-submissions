-- Write your query below
select c.name
FROM customers c
WHERE c.id NOT IN (select customer_id FROM orders)

