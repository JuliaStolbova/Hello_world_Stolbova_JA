i = 1
sum = 0

for i in range(1, 15):
    if i % 2 == 0:
        sum += i
    i += 1
print("Сумма всех четных чисел данного интервала: ", sum)
