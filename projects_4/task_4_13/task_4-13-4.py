a = [1, 3, 6, 7, 10, 5]
n = len(a)
i = 0
sum = 0

for i in range(n):
    sum = sum + a[i]
    i = i + 1

print("Сумма первых чисел: ", sum)
