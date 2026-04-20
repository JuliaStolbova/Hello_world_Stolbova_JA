update prices
set price = price * 1.1
where price < 1000;

update prices
set price = price * 1.05
where (product_id <= 5) and (price < 10000);


