import random
szamok = []
for i in range(0,10):
    szamok.append(random.randint(1,99))
for i in range(0,10):
    for o in range(0,9):
        if szamok[o+1] < szamok[o]:
            temp = szamok[o]
            szamok[o] = szamok[o+1]
            szamok[o+1] = temp

print(szamok)