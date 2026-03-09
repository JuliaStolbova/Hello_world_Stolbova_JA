#!/bin/bash

echo "Ivan 78" >> students.txt
echo "Maria 92" >> students.txt
echo "Oleg 67" >> students.txt
echo "Anna 85" >> students.txt
awk '{ print $1 }' students.txt
awk '{ print $2 }' students.txt
awk '{ print NR, $1 }' students.txt

