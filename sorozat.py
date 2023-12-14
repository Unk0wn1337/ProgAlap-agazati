import random

randomSzamLista = []
index = 0
while index < 12:
    randomSzam = random.randint(-10,1000)
    randomSzamLista.append(randomSzam)
    index+=1

def paratalon_szamak():
    paratalonSzamok = 0
    index = 0
    while index < len(randomSzamLista):
        if randomSzamLista[index] % 2 == 1:
            paratalonSzamok += 1
        index+=1
    return paratalonSzamok

def konzol_kiir():
    print(f"\nPáratlan számok: {paratalon_szamak()}")

def masodikFeladat():
    index = 0
    while index < len(randomSzamLista):
        if index == 0:
            print(randomSzamLista[index],end="")
        else:
            print(f"${randomSzamLista[index]}",end="")
        index+=1

def fajlba_kiir():
    f = open("fajlbair.txt","w",encoding="utf-8")
    f.write(f"Páratlan számok: {paratalon_szamak()}")
    f.close()
