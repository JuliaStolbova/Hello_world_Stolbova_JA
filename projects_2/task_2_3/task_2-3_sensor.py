operator = input("Введите имя оператора:").strip()
value = input("Введите текущее значение датчика давления:").strip()

log_entry = f"{operator}\t{value}\n"

with open("sensor_log.txt", "a", encoding="utf-8") as log_file:
    log_file.write(log_entry)

print("Данные успешно сохранены в sensor_log.txt")
