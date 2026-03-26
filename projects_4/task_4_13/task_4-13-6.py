a = [float(input("Введите значение: ")) for i in range(5)]
n = len(a)
i = 0
sum = 0

for i in range(n):
    sum = sum + a[i]**2
    i = i + 1

print("Сумма квадратов первых чисел: ", sum)
