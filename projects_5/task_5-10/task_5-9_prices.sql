select *
from prices 
order by price desc 
limit 5;

select *
from prices 
order by created_at
limit 10;

select price 
from prices 
order by price asc  
limit 10;

select *
from prices 
order by price desc 
offset 20;

