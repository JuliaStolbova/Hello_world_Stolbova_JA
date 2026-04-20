select *
from products;

select name, category
from products;

SELECT name 
FROM products 
WHERE category = 'Электроника';

select distinct category
from products;

select *
from products 
order by name asc;

select *
from products 
order by name desc;

select *
from products
limit 10;

select *
from products
limit 10 offset 10;

SELECT * 
FROM products 
WHERE category = 'Бытовая техника'
order by name asc
limit 15;

SELECT * 
FROM products 
ORDER BY RANDOM()
limit 5;

SELECT category 
FROM products 
order by category asc;

SELECT * 
FROM products 
order by category asc;

SELECT * 
FROM products 
order by name asc;














