class Zwierze:
    def __init__(self,jedzenie,dlugosc_zycia):
        self.jedzenie = jedzenie
        self.dlugosc_zycia = dlugosc_zycia
    def szama(self):
        print("Moim pokarmem jest : ",self.jedzenie)
    def zycie(self):
        print("Będę z tobą żyć ",self.dlugosc_zycia," lat!")
class Pies(Zwierze):
    def __init__(self, jedzenie, dlugosc_zycia,szczek):
        super().__init__(jedzenie, dlugosc_zycia)
        self.szczek = szczek
    def daj_glos(self):
        print(self.szczek)
class Kot(Zwierze):
    def __init__(self, jedzenie, dlugosc_zycia,mial):
        super().__init__(jedzenie, dlugosc_zycia)
        self.mial = mial
    def kicikici(self):
        print(self.mial)
class Ptak(Zwierze):
    def __init__(self, jedzenie, dlugosc_zycia,cwierk):
        super().__init__(jedzenie, dlugosc_zycia)
        self.cwierk = cwierk
    def kotecek(self):
        print(self.cwierk)
class Ryba(Zwierze):
    def __init__(self, jedzenie, dlugosc_zycia,bulk):
        super().__init__(jedzenie, dlugosc_zycia)
        self.bulk = bulk
    def bul(self):
        print(self.bulk)
reksio = Pies("Mięsko!",20,"HAU!")
puszek = Kot("Karma dla kotka",15,"Miał!")
twitty = Ptak("Słonecznik",3,"Plosze państwa, Kotecek!")
doris = Ryba("Plankton",2,"Bulbul Jestem pod wodą Bulbul")
print("Reksio")
reksio.szama()
reksio.zycie()
reksio.daj_glos()
print("Puszek")
puszek.szama()
puszek.zycie()
puszek.kicikici()
print("Twitty")
twitty.szama()
twitty.zycie()
twitty.kotecek()
print("Doris")
doris.szama()
doris.zycie()
doris.bul()