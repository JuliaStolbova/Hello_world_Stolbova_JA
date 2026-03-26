a = [float(input("Введите число ")) for i in range(5)]
n = len(a)
i = 0
max = a[i]
for i in range(1, n):
    if max < a[i]:    
        max = a[i]

print(max)
        