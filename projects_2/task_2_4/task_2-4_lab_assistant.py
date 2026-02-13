value_solution = int(input("Введите общий объем раствора"))
mass_salt = value_solution * 0.009
print("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
print("-------------------------\n")
print(f"Общий объем:\t {value_solution} мл")
print(f"Масса соли:\t {round(mass_salt, 2)} г")
print(f"Объем воды:\t {value_solution} мл")
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ\n")
    file.write("-----------------------------\n")
    file.write(f"Общий объем:\t {value_solution} мл\n")
    file.write(f"Масса соли:\t {round(mass_salt, 2)} г\n")
    file.write(f"Объем воды:\t {value_solution} мл\n")