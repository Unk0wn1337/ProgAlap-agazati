import  Pogyasz

def pogyasSzama():
    print("III/A,B:")
    db = 0
    f = open("csomag.txt","r",encoding="utf-8")
    f.readline()
    sorok = f.readlines()
    f.close()
    index = 0
    while index < len(sorok):
        db += 1
        index +=1
    print(f"\tA pogyászok száma {db} ")
    print("III/C")
    index = 0
    gram = 0
    while index < len(sorok):
        Csomag = Pogyasz.Pogyasz(sorok[index])
        if Csomag.szelesseg == 51:
            gram += Csomag.suly
        index += 1
    print(f"\tAz 51 cm-es pogyászok átlag súlyértéke: {gram} g")
    index = 0
    maxMagassag = 0
    maxHely = 0
    while index < len(sorok):
        Csomag = Pogyasz.Pogyasz(sorok[index])
        if Csomag.magassag > maxMagassag:
            maxMagassag = Csomag.magassag
            maxHely = index

        index+=1
    print("III/D")
    print(f"\tA legmagasabb pogyász méretei:  {maxHely} kg {maxHely}            ")








