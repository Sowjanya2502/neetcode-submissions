-- Write your query below
select seller_name
FROM seller
WHERE seller_id NOT IN (select o.seller_id FROM orders o WHERE EXTRACT(YEAR FROM sale_date) = 2020)
ORDER BY seller_name