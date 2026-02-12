name = input("Название питательной среды:")
concentration = input("Концентрация агара(%):")
temperature = input("Температура стерилизации (°С):")

print(f"Название питательной среды: {name}\nКонцентрация агара: {concentration}\nТемпература стерилизации: {temperature}\n")
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"Название питательной среды: {name}\nКонцентрация агара: {concentration}\nТемпература стерилизации: {temperature}\nФайл `recipe.txt` успешно сформирован!")
