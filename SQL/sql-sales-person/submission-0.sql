-- Write your query below
select name
FROM sales_person
WHERE sales_id NOT IN (
    select sales_id 
    FROM orders 
    LEFT JOIN company ON orders.com_id = company.com_id
    WHERE company.name = 'CRIMSON');