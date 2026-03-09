#!/bin/bash

df -h >> an.txt
awk 'NR>2 {print $1, $5 }' an.txt
awk '{
	if ( $5 > 90.0 )
		print "Место заканчивается. Очистите папку"
	else 
		print "Все хорошо, можете скачивать еще и еще!"
}' an.txt

