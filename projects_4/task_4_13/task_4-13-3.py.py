a = [float(input("Введите 5 чисел через enter: ")) for i in range(5)]
n = len(a)
i = 0
pr = 1

for i in range(n):
    pr= pr*a[i]

print("Факториал для n равен: ", pr)