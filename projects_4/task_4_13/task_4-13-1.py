x = float(input("введите значение числа X: "))
y = float(input("введите значение числа Y: "))
z = float(input("введите значение числа Z: "))
q = float(input("введите значение числа Q: "))
max = x

if max < y: 
    max = y
if max < z:
    max = z
if max < q:
    max = q
print("Максимальное значение: ", max)