select product_id, count(*)
from suppliers
group by product_id
order by product_id asc;


