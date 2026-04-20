select 	
p.name,
pr.price
from products as p
join prices as pr on p.id = pr.id;


