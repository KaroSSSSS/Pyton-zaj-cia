class Restaurant:
    def __init__(self,nazwa,lokacja):
        self.nazwa = nazwa
        self.lokacja = lokacja
class IceCreamStand(Restaurant):
    def __init__(self, nazwa, lokacja,menu_lodzikow):
        super().__init__(nazwa, lokacja)
        self.menu_lodzikow = menu_lodzikow
    def smaki(self):
        print("To są dostępne smaki w lodziarni: ")
        print(self.menu_lodzikow)
    def mieszanie(self):
        print("Witaj w mieszalni smaków lodów!")
        print("Powiedz proszę, jakie smaki chcesz mieć w lodach:")
        print(self.menu_lodzikow)
        wybor = int(input("Wybierz je prosze po indeksach z listy wyżej.Dla wszystkich smaków wybierz proszę opcję 4 Jeśli skończyłeś mieszanie, wybierz proszę opcje 0.\n"))
        if wybor != 0:
            if wybor == 1:
                print("Wybrałeś smak :",smakilodziarnia[0])
                smaki = smakilodziarnia[0]
                wybor2 = int(input("Wybierz proszę kolejny smak"))
                if wybor2 == 1:
                    print("Już wybrałeś ten smak, kończę mieszanie")
                elif wybor2 == 2:
                    print("Wybrałeś smak :",smakilodziarnia[1], "Dodaję do mieszanki")
                    smaki += smakilodziarnia[1]
                elif wybor2 == 3:
                    print("wybrałeś smak :",smakilodziarnia[2],"Dodaję do mieszanki")
                    smaki += smakilodziarnia[2]
                else:
                    print("Nie ma takiego smaku w mojej lodziarni")
                    pass
            if wybor == 2:
                print("Wybrałeś smak :",smakilodziarnia[1])
                smaki = smakilodziarnia[1]
                wybor2 = int(input("Wybierz proszę kolejny smak"))
                if wybor2 == 1:
                    print("Wybrałeś smak :",smakilodziarnia[0], "Dodaję do mieszanki")
                    smaki += smakilodziarnia[0]
                elif wybor2 == 2:
                    print("Już wybrałeś ten smak, kończę mieszanie")
                elif wybor2 == 3:
                    print("wybrałeś smak :",smakilodziarnia[2],"Dodaję do mieszanki")
                    smaki += smakilodziarnia[2]
                else:
                    print("Nie ma takiego smaku w mojej lodziarni")
                    pass
            if wybor == 3:
                print("Wybrałeś smak :",smakilodziarnia[2])
                smaki = smakilodziarnia[2]
                wybor2 = int(input("Wybierz proszę kolejny smak"))
                if wybor2 == 1: 
                    print("Wybrałeś smak :",smakilodziarnia[0], "Dodaję do mieszanki")
                    smaki += smakilodziarnia[0]
                    
                elif wybor2 == 2:
                    print("wybrałeś smak :",smakilodziarnia[1],"Dodaję do mieszanki")
                    smaki += smakilodziarnia[1]
                elif wybor2 == 3:
                    print("Już wybrałeś ten smak, kończę mieszanie")
                else:
                    print("Nie ma takiego smaku w mojej lodziarni")
            if wybor == 4:
                smaki = smakilodziarnia
                print("Wybrałeś wszystkie smaki!")
        else:
            pass
        print("Twoje smaki :",smaki)

class Coffeshop(Restaurant):
    def __init__(self, nazwa, lokacja,menu_kaw,cenykaw,menuciasteczek,cenaciasteczek):
        super().__init__(nazwa, lokacja)
        self.menu_kaw = menu_kaw
        self.cenykaw = cenykaw
        self.menuciasteczek = menuciasteczek
        self.cenaciasteczek = cenaciasteczek
    def menukawusi(self):
        print("Takie mamy kawy w naszej kawiarni :\n",menukaw)
    def LICZYMYCENY(self):
        #1 etap, zamawiamy kaWUsie
        print("Witaj w kawiarni! Tu masz listę kaw, wybierz proszę, jaką chcesz zamówić\n", menukaw,"\n oraz ich ceny\n",cenakaw)
        wyborkawy = str(input())
        if wyborkawy == "americano":
            print("Wybrałeś kawę ",menukaw[0],"o cenie ",cenakaw[0] )
            zamowienie = menukaw[0]
            cena_zamowienia = cenakaw[0]
        elif wyborkawy == "latte":
            print("Wybrałeś kawę ",menukaw[1],"o cenie ",cenakaw[1] )
            zamowienie = menukaw[1]
            cena_zamowienia = cenakaw[1]
        elif wyborkawy == "mocha":
            print("Wybrałeś kawę ",menukaw[2],"o cenie ",cenakaw[2] )
            zamowienie = menukaw[2]
            cena_zamowienia = cenakaw[2]
        elif wyborkawy == "zwykła":
            print("Wybrałeś kawę ",menukaw[3],"o cenie ",cenakaw[3] )            
            zamowienie = menukaw[3]
            cena_zamowienia = cenakaw[3]
        print("To teraz czy chcesz ciasteczko do kawy? Tak/Nie")
        odpowiedz = str(input())
        if odpowiedz == "Tak" or "tak":
            print("To tutaj masz listę ciasteczek \n",menuciasteczek,"\n i ich cen \n",cenaciasteczek,"Wybierz sobie!")
            wyborciastek = str(input())
            if wyborciastek == "tani herbatnik":
                print("Czyli chcesz zwykły herbatnik, biedaku? To masz!", cenaciasteczek[0])
                zamowienie += menuciasteczek[0]
                cena_zamowienia += cenaciasteczek[0]
            elif wyborciastek == "herbatnik z czekoladą":
                print("O prosze! Z czekoladą? To masz!", cenaciasteczek[1])
                zamowienie += menuciasteczek[1]
                cena_zamowienia += cenaciasteczek[1]
            elif wyborciastek == "CIASTO":
                print("CIASTOOOOOOOOO", cenaciasteczek[2])
                zamowienie += menuciasteczek[2]
                cena_zamowienia += cenaciasteczek[2]
        else:
            print("Nie to nie, sama kawa")
        #kasa
        print("Twoje zamówienie :", zamowienie)
        print("I cena tego zamówienia :", cena_zamowienia)
#Lista menu 

smakilodziarnia = ["1. Waniliowe","2. Czekoladowe","3. Truskawkowe"]

menukaw = ["americano","latte","mocha","zwykła a nie jakieś wymysły z wyższej półki"]
cenakaw = [10.50,11.50,16.90,11.50]
menuciasteczek = [" tani herbatnik"," herbatnik ale z czekoladą to już lepszy"," CIASTO"]
cenaciasteczek = [0.50,1.00,5.00]
#lista obiektów
Lodziarnia = IceCreamStand("Lody dla ochłody","Centrum miasta", smakilodziarnia)
Lodziarnia.smaki()
Lodziarnia.mieszanie()

kawiarnia = Coffeshop("Duża biała","Rondo wyzwolenia niewolników żydowskich", menukaw,cenakaw,menuciasteczek,cenaciasteczek)
kawiarnia.menukawusi()
kawiarnia.LICZYMYCENY()
