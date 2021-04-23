class sklep:
    def init(self, nazwapiwa, procenty, opakowanie, cena, miejsce):
        self.nazwapiwa = nazwapiwa
        self.procenty = procenty
        self.opakowanie = opakowanie
        self.cena = cena
        self.miejsce = miejsce
class beer(sklep):
    def init(self, nazwapiwa, procenty, opakowanie, cena, miejsce):
        super().init(nazwapiwa, procenty, opakowanie, cena, miejsce)
    def kupnopiwka(self):
        print("Czy na pewno chcesz kupić piwko: ",self.nazwapiwa,"?")
        potwierdzenie = input(" Tak/Nie ")
        if potwierdzenie == "Tak" or potwierdzenie =="tak":
            if self.miejsce == "bar":
                print("Należy się", self.cena+2,"zł")
            elif self.miejsce == "sklep":
                print("Należy się",self.cena,"zł")
        else:
            print("To nie zawracaj mi gitary")
Kasztelan = beer("Kasztelan","6%","butelka",6,"bar")

Kasztelan.kupnopiwka()