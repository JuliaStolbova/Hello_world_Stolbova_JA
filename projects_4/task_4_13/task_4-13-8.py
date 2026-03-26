a = [float(input("Введите числа: ")) for i in range(10)]
n = len(a)
i = 0
count  = 0
for i in range(n):
    if a[i] > 0:
        count = count + 1
    i = i + 1
print("Количество положительных чисел в массиве: ", count)

    