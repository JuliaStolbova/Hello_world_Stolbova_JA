select *
from products
WHERE category = 'Электроника';

select *
from products
WHERE category = 'Одежда' and name like '%женские%';

select *
from products
WHERE category = 'Продукты' or category = 'Книги';

select *
from products
WHERE not category = 'Бытовая техника';

select *
from products
WHERE category = 'Электроника' or category = 'Одежда' or category = 'Книги';

SELECT * 
FROM products 
WHERE category = 'Электроника' AND name LIKE '%Samsung%';

SELECT * 
FROM products 
WHERE (category = 'Электроника' AND name LIKE '%Samsung%') or category = 'Бытовая техника';

SELECT * 
FROM products 
WHERE (category = 'Электроника' or category = 'Бытовая техника' or category = 'Одежда') and (id between 1 and 15) and not name LIKE '%Samsung%';

SELECT * 
FROM products 
WHERE ((category = 'Электроника' or category = 'Бытовая техника' or category = 'Одежда') and (id between 1 and 15) and (not name LIKE '%Samsung%')) or (category = 'Книги');


