name = input("ФИО исследователя:")
data = input("Дата:")
name_ex= input("Название эксперимента:")
result = input("Выводы")
with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("+----------------------------------+\n")
    file.write("|Электронный лабораторный журнал   |\n")
    file.write("+----------------------------------+\n")
    file.write(f"|ФИО исследователя : {name} |\n")
    file.write(f"|Дата : {data}                |\n")
    file.write(f"|Название эксперимента : {name_ex}  |\n")
    file.write(f"|Выводы : {result}|\n")
    file.write("+----------------------------------+")


