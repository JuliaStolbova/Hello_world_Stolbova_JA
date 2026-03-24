a = [7, 3, 8, 1, 4, 6, 2, 5]
n = len(a)

for i in range(n):
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print("Отсортированный массив: ", a)