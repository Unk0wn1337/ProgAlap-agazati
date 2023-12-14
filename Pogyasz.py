# a#b#c#m
# 51#33#24#10

class Pogyasz:
    def __init__(self, sor: str):
        adatok = sor.strip().split("#")
        self.szelesseg = int(adatok[0])
        self.magassag = int(adatok[1])
        self.melyseg = int(adatok[2])
        self.suly = int(adatok[3])