class AUTKO:
    def __init__(self,marka,cena,kolor,rodzaj,stan_licznika):
        self.marka = marka
        self.cena = cena
        self.kolor = kolor
        self.rodzaj = rodzaj
        self.stan_licznika = stan_licznika
    def jaki_przebieg(self):
        return "Auto ma {} przebieg".format(self.stan_licznika)
    def jaki_kolor(self):
        return "Auto ma {} kolor".format(self.kolor)
    def jaka_marka(self):
        return "Auto jest {} marki".format(self.marka)
    def jaki_rodzaj(self):
        return "Auto jest {}em".format(self.rodzaj)
    def jaka_cena(self):
        return "Auto jest warte {} zł".format(self.cena)
    def Krzychu(self):
        return "KRZYCHU KADETEM DAWAJ"
ferrari = AUTKO("Ferrari", 1200000, "Czerwony", "Sedan", 4201337)
opel = AUTKO("OPEL KADET","mało","Czerwono-wiśniowy", "Najlepsz","jaki pan chce")
print(ferrari.jaki_przebieg())
print(ferrari.jaki_kolor())
print(ferrari.jaka_marka())
print(ferrari.jaki_rodzaj())
print(ferrari.jaka_cena())
print(opel.jaki_przebieg())
print(opel.jaki_kolor())
print(opel.jaka_marka())
print(opel.jaki_rodzaj())
print(opel.jaka_cena())
print(opel.Krzychu())