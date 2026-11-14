woerter = ["Katze", "Elefant", "Hund", "Nilpferd"]
vorkommende_laengen = {len(wort) for wort in woerter}
print("==={len(wort) for wort in woerter}=====1==\n")
print(vorkommende_laengen) # {8, 4, 5, 7}

woerter = ["Katze", "Elefant", "Hund", "Nilpferd"]
print("=====(wort: len(wort)===2======\n")
laengen = {wort: len(wort) for wort in woerter}
print(laengen)
{'Katze': 5, 'Elefant': 7, 'Hund': 4, 'Nilpferd': 8}

print("=====(len(wort)===3======\n")
laengene = {len(wort) for wort in woerter}
print(laengene)
#{8, 4, 5, 7}

print("========matrix=====4==========\n")
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flach = [zahl for zeile in matrix for zahl in zeile]
print(flach)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("=========for====5=======")
flach = []
for zeile in matrix:
    for zahl in zeile:
        flach.append(zahl)
        print(flach)
#[1]
#[1, 2]
#[1, 2, 3]
#[1, 2, 3, 4]
#[1, 2, 3, 4, 5]
#[1, 2, 3, 4, 5, 6]
#[1, 2, 3, 4, 5, 6, 7]
#[1, 2, 3, 4, 5, 6, 7, 8]
#[1, 2, 3, 4, 5, 6, 7, 8, 9]