#!/bin/bash

echo "1,Mouse,23" >> data.csv
echo "2,Keyboard,15" >> data.csv
echo "3,Monitor,120" >> data.csv
echo "4,USB,5" >> data.csv
awk -F "," '{print $2}' data.csv
awk -F "," '$3>20 {print $2, $3}' data.csv
awk -F "," '{sum += $3} END {print sum}' data.csv

