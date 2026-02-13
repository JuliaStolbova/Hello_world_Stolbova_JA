weight = int(input("Введите ваш вес (кг):"))
high = int(input("Введите ваш рост (см):"))
bmi = (weight)/(high**2)

print("-- Отсчет о состоянии пациента --\n")
print(f"Рост:\t {weight}\n")
print(f"Вес:\t {high}\n")
print("Индекс массы тела:")
print(bmi)
