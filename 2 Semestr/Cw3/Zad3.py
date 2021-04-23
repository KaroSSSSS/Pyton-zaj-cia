
class Obywatel:
    def init(self,imie, nazwisko, ulica, nrDomu, kodPocztowy,miejscowosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.ulica = ulica
        self.nrDomu = nrDomu
        self.kodPocztowy = kodPocztowy
        self.miejscowosc = miejscowosc
    def PaniObywatelka(self):
        print("---------------\n",self.imie,"\n",self.nazwisko,"\n",self.ulica,"\n",self.nrDomu,"\n",self.kodPocztowy,"\n",self.miejscowosc,"\n","---------------")
    def Wpisywanie(self):
        file = open("showcase.txt", "w")
        file.write(
            f"---------------------\n{self.imie} {self.nazwisko}\nul.{self.ulica} {self.nrDomu}\n{self.kodPocztowy} {self.miejscowosc}\n---------------------"
        )

        file.close()



Paulina = Obywatel(input("Imie: "),input("Nazwisko: "),input("Ulica: "),input("nrDomu: "),input("kodPocztowy: "),input("Miejscowość: "))
Paulina.Wpisywanie()