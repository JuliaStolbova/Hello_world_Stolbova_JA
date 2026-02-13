
dna = input("Введите последовательность ДНК:")
dna_up = dna.upper()
print("=== Анализ последовательности ДНК ===\n")
print(f"Введите последовательность ДНК: {dna}\n")
print(f"Последовательность в верхнем регистре: {dna_up}\n")
print("Подсчет нуклеотидов:\n")
count_A = dna_up.count("A")
count_C = dna_up.count("C")
count_T = dna_up.count("T")
count_G = dna_up.count("G")
all_ng = count_A + count_G + count_C + count_T
total_up = len(dna_up)
procent_A = (count_A/total_up)*100
procent_C = (count_C/total_up)*100
procent_T = (count_T/total_up)*100
procent_G = (count_G/total_up)*100
print(f"A: {count_A}\n")
print(f"C: {count_C}\n")
print(f"T: {count_T}\n")
print(f"G: {count_G}\n")
print(f"Общая длина: {all_ng} нуклеотидов.\n")
print(f"Процентное содержание А: {round(procent_A, 2)}%\n")
print(f"Процентное содержание C: {round(procent_C, 2)}%\n")
print(f"Процентное содержание T: {round(procent_T, 2)}%\n")
print(f"Процентное содержание G: {round(procent_G, 2)}%")
