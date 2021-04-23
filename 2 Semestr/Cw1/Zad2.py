import operator
class Ksiazka:
    def __init__(self,gatunek,tytul,autor,dlugosc,cena):
        self.gatunek = gatunek
        self.cena = cena
        self.tytul = tytul
        self.autor = autor
        self.dlugosc = dlugosc
        
        def jaki_gatunek():
            return "Książka jest gatunku {}".format(self.gatunek)
        def jaka_cena():
            return "Książka ma cenę {} zł".format(self.cena)
        def jaki_tytul():
            return "Książka ma tytuł {}".format(self.tytul)
        def jaki_autor():
            return "Autorem książki jest {}".format(self.autor)
        def jaka_dlugosc():
            return "Książka ma {} stron".format(self.dlugosc)
def sorttitle(elem):
    return elem.tytul
##lista książek
lista_ksiazek = []
lista_ksiazek.append(Ksiazka("Opowiadanie grozy / Horror","Zew Cthulu","H.P. Lovecraft","308","30,99"))
lista_ksiazek.append(Ksiazka("Fantasy","Warcraft : Durotan", "Christie Golden", "216","24,90"))
lista_ksiazek.append(Ksiazka("Fantasy","World of Warcraft : Illidan","William King", "317","29.15"))
lista_ksiazek.append(Ksiazka("Fantasy","Wiedźmin - Sezon Burz","Andrzej Sapkowski","318","32,19"))

sorted_lista_ksiazek = lista_ksiazek.sort(key=sorttitle)
print("1.Sortowanie wg tytułu")
print("2.Wyświetlenie listy książek")
wybor = int(input("Podaj wybór:"))
if wybor == "1":
    print(sorted_lista_ksiazek)
else:
    print(lista_ksiazek)