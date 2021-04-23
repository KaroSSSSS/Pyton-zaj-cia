import time
class Figura:
    def __init__(self) -> None:
        pass
    #nie miałem pomysłu na dziedziczenie tylko. nei pasowało mi do mojego konceptu
class kwadrat(Figura):
    def __init__(self,bok):
        self.bok = bok
    def pole1(self):
        #print("qwqrweqewr") debug :)
        polekw = self.bok*self.bok
        return polekw
    def obwod1(self):
        obwodkw = 4*self.bok
        return obwodkw
class prostokat(Figura):
    def __init__(self,bok1,bok2):
        self.bok1 = bok1
        self.bok2 = bok2
    def pole2(self):
        #print("qwqrweqewr") debug :)
        polepr = self.bok1*self.bok2
        return polepr
    def obwod2(self):
        obwodpr = 2*self.bok1 + 2*self.bok2
        return obwodpr

class trojkat(Figura):
    def __init__(self,bok1,bok2,bok3,wysokosc):
        self.bok1 = bok1
        self.bok2 = bok2
        self.bok3 = bok3
        self.wysokosc = wysokosc
    def pole3(self):
        #print("qwqrweqewr") debug :)
        poletr = (self.bok1 * self.wysokosc)/2
        return poletr
    def obwod3(self):
        obwodtr = self.bok1 + self.bok2 + self.bok3
        return obwodtr

class kolo(Figura):
    def __init__(self,promien):
        self.promien = promien
    def pole4(self):
        #print("qwqrweqewr") debug :)
        polekola = 3.14*self.promien*self.promien
        return polekola
    def obwod4(self):
        obwodkola = 2*3.14*self.promien
        return obwodkola

class romb(Figura):
    def __init__(self,bok,przekatna1,przekatna2):
        self.bok = bok
        self.przekatna1 = przekatna1
        self.przekatna2 = przekatna2
    def pole5(self):
        #print("qwqrweqewr") debug :)
        polerombu = (self.przekatna1 * self.przekatna2)/2 
        return polerombu
    def obwod5(self):
        obwodrombu = 4*self.bok
        return obwodrombu
class trapez(Figura):
    def __init__(self,podstD,podstG,wysokosc,ramie1,ramie2):
        self.podstD = podstD
        self.podstG = podstG
        self.wysokosc = wysokosc
        self.ramie1 = ramie1
        self.ramie2 = ramie2
    def pole6(self):
        #print("qwqrweqewr") debug :)
        poletrapezu = ((self.podstG+self.podstD)*self.wysokosc)/2
        return poletrapezu
    def obwod6(self):
        obwodtrapezu = self.podstG+self.podstD+self.ramie1+self.ramie2
        return obwodtrapezu
#menu
print("Witaj w moim programie! Centrum figur geometrycznych i zabawy z klasami!")
time.sleep(2)
print("Zasiądź w fotelu i zapoznaj się z nim proszę!")
time.sleep(2)
print("A tutaj masz menu:")
time.sleep(1)
#lista figur
print("1. Kwadrat \n2. Prostokąt \n3.Trójkąt \n4. Koło \n5. Romb \n6. Trapez")
wybor1 = int(input("Podaj liczbę odpowiadajacą twojemu wyborowi\n"))
if wybor1 == 1:
    print("Wybrano kwadrata.\nProszę wprowadzić wymiar:")
    #tworze obiekt tutaj, żeby użyć klasy do obliczenia pola
    oblicz = kwadrat(int(input("Podaj długość boku")))
    print("Dziękuję. Przystępuję do obliczenia pola i obwodu.")
    print("Pole kwadratu wynosi:",oblicz.pole1())
    print("Obwód kwadratu wynosi:",oblicz.obwod1())
    
elif wybor1 == 2:
    print("Wybrano prostokąt.\nProszę wprowadzić wymiary:")
    #tworze obiekt tutaj, żeby użyć klasy do obliczenia pola
    oblicz2 = prostokat(int(input("Podaj długość boku A: ")),int(input("Podaj długość boku B: ")))
    print("Dziękuję. Przystępuję do obliczenia pola i obwodu.")
    print("Pole prostokąta wynosi:",oblicz2.pole2())
    print("Obwód prostokąta wynosi:",oblicz2.obwod2())
    
elif wybor1 == 3:
    print("Wybrano trójkąt. \nProszę wprowadzić wymiary:")
    #tworze znów tutaj
    oblicz3 = trojkat(int(input("Bok A: ")),int(input("Bok B: ")),int(input("Bok C: ")),int(input("Wysokość: ")))
    print("Dziękuję. Przystępuję do obliczenia pola i obwodu.")
    print("Pole trójkąta wynosi: ",oblicz3.pole3())
    print("Obwód trójkąta wynosi: ",oblicz3.obwod3())
elif wybor1 == 4:
    print("Wybrano koło.\nProsze wprowadzić wymiary:")
    #I znowu
    oblicz4= kolo(int(input("Podaj promień: ")))
    print("Dziękuję. Przystępuję do obliczenia pola i obwodu.")
    print("Pole koła wynosi: ",oblicz4.pole4())
    print("Obwód koła wynosi: ",oblicz4.obwod4())
elif wybor1 == 5:
    print("Wybrano romb.\n Proszę wprowadzić wymiary:")
    #I jeszcze raz!
    oblicz5 = romb(int(input("Prosze podaj długość boku: ")),int(input("Proszę podaj długość pierwszej przekątnej: ")),int(input("Proszę podaj długość drugiej przekątnej: ")))
    print("Dziękuję. Przystępuję do obliczenia pola i obwodu.")
    print("Pole rombu wynosi: ",oblicz5.pole5())
    print("Obwód rombu wynosi: ",oblicz5.obwod5())
elif wybor1 == 6:
    print("Wybrano trapez.\n Proszę wprowadzić wymiary: ")
    #I ostatni raz
    oblicz6 = trapez(int(input("Proszę podaj długość dolnej podstawy: ")),int(input("Proszę podaj długość górnej postawy: ")),int(input("Prosze podaj wysokość: ")),int(input("Proszę podaj długość pierwszego ramienia: ")),int(input("Prosze podaj długość drugiego ramienia: ")))
    print("Dziękuję. Przystępuję do obliczenia pola i obwodu.")
    print("Pole trapezu wynosi: ",oblicz6.pole6())
    print("Obwód trapezu wynosi: ",oblicz6.obwod6())
else:
    print("Nie ma takiego wyboru. Zamykam")
    exit()