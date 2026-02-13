number = int(input("Введите общее количество произведенных капсул:"))
number_2 = int(input("Вместимость одной упаковки:"))
full_number = number//number_2
end_number = number%number_2
print("--- Отчет фасовочного цеха ---")
print(f" Полных упаковок: {full_number}")
print(f"Полных упаковок: {end_number}")
