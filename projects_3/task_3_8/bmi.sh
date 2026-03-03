#!/bin/bash

read -p "Введите свой вес в кг: " WEIGHT
read -p "Введите свой роств  метрах: " HIGH

BMI=$(((WEIGHT/HIGH^2)*10))


echo "Ваш индекс массы тела составляет $BMI "

