#!/bin/bash

for i in {1..10}; do
    echo "${i}.txt" > test${i}.txt
done

i=10
while [ $i -ge 1 ]; do
    rm test${i}.txt
    echo "${i}.txt"
    ((i--))
done

