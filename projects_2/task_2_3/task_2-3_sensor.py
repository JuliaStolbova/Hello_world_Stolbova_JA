operator = input("Введите имя оператора:").strip()
value = input("Введите текущее значение датчика давления (Па):").strip()


with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write(f"Введите имя оператора:{operator}\nвведите текущее значение датчика давления (Па):{value}\nДанные успешно сохранены в sensor_log.txt")