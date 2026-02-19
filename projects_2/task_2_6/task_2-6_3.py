phenotype_d = input("Введите группу крови донора (I, II, III, IV, 0): ").strip().upper()
phenotype_r = input("Введите группу крови реципиента (I, II, III, IV): ").strip().upper()
if phenotype_d == phenotype_r:
    print("Переливание возможно")
if phenotype_d == 0:
    print("Переливание возможно")
if  phenotype_d != phenotype_r or phenotype_d != 0:
    print("Переливание не возможно")

     
    