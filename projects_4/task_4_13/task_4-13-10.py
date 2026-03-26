a = [float(input("Введите числа: ")) for i in range(7)]
n = len(a)
i = 0
sum = 0

for i in range(n):
    if i%2 == 1:
        sum = sum + a[i]
    i = i + 1

print("Сумма нечетных элементов: ", sum)
        