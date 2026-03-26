a = [1, 5, 8, 9, 5, 3, 5]
n = len(a)
i = 0
sum = 0

for i in range(n):
    sum = sum + a[i]
    i = i + 1

avg = sum/n
print("Среднее арифметическое чисел: ", round(avg))