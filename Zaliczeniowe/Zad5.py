#Waluty ze strony cinkciarz.pl i kantor-walut.pl
#Dla kryptowalut jest jeden kurs kupna i sprzedaży
import time  # w sumie to nie, bo maiłem pomysł, ale nie wypalił, bo w pytongu nie ma switcha, a moja imitacja ze słownikami i listami nie działała hmmm...

#Zmienne

THB_K = 0.0332
THB_S = 0.0342
BTC_K = 35760.3
BTN_K = 0.0495
BTN_S = 0.0522
MRO_K = 0.0028
MRO_S = 0.0030
ETH_K = 1388.8
DOGE_K = 0.3413
ILS_K = 0.3005
ILS_S = 0.3085
ZAR_K = 0.0630
ZAR_S = 0.0692

#Funkcje
def THB_zakup():
    global THB_K
    ilosc = int(input("Podaj ile THB chcesz zakupić:"))
    cena = ilosc * THB_K
    print("Będzie CIę to kosztować ", round(cena,2),"USD")

def THB_sprzedaz():
    global THB_S
    ilosc = int(input("Podaj ile THB chcesz sprzedać:"))
    cena = ilosc * THB_S
    print("Dostaniesz ", round(cena,2),"USD")

def THB():
    print("wybrałeś THB")
    print("Chcesz kupić, czy sprzedać? K / S")
    wybor_2 = input()
    if wybor_2 =="K" or wybor_2 =="Kupić":
        THB_zakup()
    elif wybor_2 =="S" or wybor_2 =="Sprzedać":
        THB_sprzedaz()
    else:
        print("Nie ma takiego wyboru")

def BTC_zakup():
    global BTC_K
    ilosc = int(input("Podaj ile BTC chcesz zakupić:"))
    cena = ilosc * BTC_K
    print("Będzie CIę to kosztować ", round(cena,2),"USD")

def BTC_sprzedaz():
    global BTC_K
    ilosc = int(input("Podaj ile BTC chcesz sprzedać:"))
    cena = ilosc * BTC_K
    print("Dostaniesz ", round(cena,2),"USD")

def BTC():
    print("wybrałeś BTC")
    print("Chcesz kupić, czy sprzedać? K / S")
    wybor_2 = input()
    if wybor_2 =="K" or wybor_2 =="Kupić":
        BTC_zakup()
    elif wybor_2 =="S" or wybor_2 =="Sprzedać":
        BTC_sprzedaz()
    else:
        print("Nie ma takiego wyboru")

def BTN_zakup():
    global BTN_K
    ilosc = int(input("Podaj ile BTN chcesz zakupić:"))
    cena = ilosc * BTN_K
    print("Będzie CIę to kosztować ", round(cena,2),"USD")

def BTN_sprzedaz():
    global BTN_S
    ilosc = int(input("Podaj ile BTN chcesz sprzedać:"))
    cena = ilosc * BTN_S
    print("Dostaniesz ", round(cena,2),"USD")

def BTN():
    print("wybrałeś BTN")
    print("Chcesz kupić, czy sprzedać? K / S")
    wybor_2 = input()
    if wybor_2 =="K" or wybor_2 =="Kupić":
        BTN_zakup()
    elif wybor_2 =="S" or wybor_2 =="Sprzedać":
        BTN_sprzedaz()
    else:
        print("Nie ma takiego wyboru")

def MRO_zakup():
    global MRO_K
    ilosc = int(input("Podaj ile MRO chcesz zakupić:"))
    cena = ilosc * MRO_K
    print("Będzie CIę to kosztować ", round(cena,2),"USD")

def MRO_sprzedaz():
    global MRO_S
    ilosc = int(input("Podaj ile MRO chcesz sprzedać:"))
    cena = ilosc * MRO_S
    print("Dostaniesz ", round(cena,2),"USD")

def MRO():
    print("wybrałeś MRO")
    print("Chcesz kupić, czy sprzedać? K / S")
    wybor_2 = input()
    if wybor_2 =="K" or wybor_2 =="Kupić":
        MRO_zakup()
    elif wybor_2 =="S" or wybor_2 =="Sprzedać":
        MRO_sprzedaz()
    else:
        print("Nie ma takiego wyboru")

def ETH_zakup():
    global ETH_K
    ilosc = int(input("Podaj ile ETH chcesz zakupić:"))
    cena = ilosc * ETH_K
    print("Będzie CIę to kosztować ", round(cena,2),"USD")

def ETH_sprzedaz():
    global ETH_K
    ilosc = int(input("Podaj ile ETH chcesz sprzedać:"))
    cena = ilosc * ETH_K
    print("Dostaniesz ", round(cena,2),"USD")

def ETH():                                                          #Coś miałem tu wpisać
    print("wybrałeś ETH")                                           #Ale zapomniałem co
    print("Chcesz kupić, czy sprzedać? K / S")                      #
    wybor_2 = input()                                               # LOL
    if wybor_2 =="K" or wybor_2 =="Kupić":
        ETH_zakup()
    elif wybor_2 =="S" or wybor_2 =="Sprzedać":
        ETH_sprzedaz()
    else:
        print("Nie ma takiego wyboru")

def DOGE_zakup():
    global DOGE_K
    ilosc = int(input("Podaj ile DOGE chcesz zakupić:"))
    cena = ilosc * DOGE_K
    print("Będzie CIę to kosztować ", round(cena,2),"USD")

def DOGE_sprzedaz():
    global DOGE_K
    ilosc = int(input("Podaj ile DOGE chcesz sprzedać:"))
    cena = ilosc * DOGE_K
    print("Dostaniesz ", round(cena,2),"USD")

def DOGE():
    print("wybrałeś DOGE")
    print("Chcesz kupić, czy sprzedać? K / S")
    wybor_2 = input()
    if wybor_2 =="K" or wybor_2 =="Kupić":
        DOGE_zakup()
    elif wybor_2 =="S" or wybor_2 =="Sprzedać":
        DOGE_sprzedaz()
    else:
        print("Nie ma takiego wyboru")

def ILS_zakup():
    global ILS_K
    ilosc = int(input("Podaj ile ILS chcesz zakupić:"))
    cena = ilosc * ILS_K
    print("Będzie CIę to kosztować ", round(cena,2),"USD")

def ILS_sprzedaz():
    global ILS_S
    ilosc = int(input("Podaj ile ILS chcesz sprzedać:"))
    cena = ilosc * ILS_S
    print("Dostaniesz ", round(cena,2),"USD")

def ILS():
    print("wybrałeś ILS")
    print("Chcesz kupić, czy sprzedać? K / S")
    wybor_2 = input()
    if wybor_2 =="K" or wybor_2 =="Kupić":
        ILS_zakup()
    elif wybor_2 =="S" or wybor_2 =="Sprzedać":
        ILS_sprzedaz()
    else:
        print("Nie ma takiego wyboru")

def ZAR_zakup():
    global ZAR_K
    ilosc = int(input("Podaj ile ZAR chcesz zakupić:"))
    cena = ilosc * ZAR_K
    print("Będzie CIę to kosztować ", round(cena,2),"USD")

def ZAR_sprzedaz():
    global ZAR_S
    ilosc = int(input("Podaj ile ZAR chcesz sprzedać:"))
    cena = ilosc * ZAR_S
    print("Dostaniesz ", round(cena,2),"USD")

def ZAR():
    print("wybrałeś ZAR")
    print("Chcesz kupić, czy sprzedać? K / S")
    wybor_2 = input()
    if wybor_2 =="K" or wybor_2 =="Kupić":
        ZAR_zakup()
    elif wybor_2 =="S" or wybor_2 =="Sprzedać":
        ZAR_sprzedaz()
    else:
        print("Nie ma takiego wyboru")
#array do pseudo switcha - już nie, bo nie działo tak jak bym chciał , żeby działo. Zrobiłem ifami.
def wybor(waluta):
    if waluta == "THB":
        THB()
    elif waluta == "BTC":
        BTC()
    elif waluta == "BTN":
        BTN()
    elif waluta == "MRO":
        MRO()
    elif waluta == "ETH":
        ETH()
    elif waluta == "DOGE":
        DOGE()
    elif waluta == "ILS":
        ILS()
    elif waluta == "ZAR":
        ZAR()
    else:
        print("Nie ma takiej waluty")



#Interakcja z użytkownikiem
print("Witaj w moim programie wymiany walut!")
print("Oferujemy wymiany w następujących walutach:")
print("1. THB - USD 0.0332 K | S 0.0342")
print("2. BTC - USD K | S 35760.30")
print("3. BTN - USD 0.0495 K | S 0.0522")
print("4. MRO - USD 0.0028 K | S 0.0030")
print("5. ETH - USD K | S 1388.8")
print("6. DOGE - USD K | S 0.3413")       # dodatkowa waluta, dogecoin. Kryptowaluta.
print("7. ILS - USD 0.3005 K | S 0.3085") # dodatkowa waluta, żydowski szekel
print("8. ZAR - USD 0.0630 K | S 0.0692") # dodatkowa waluta, rand południowoafrykański

print("Zdradź mi proszę, na jakiej walucie chcesz przeprowadzać operacje? Użyj proszę skrótów podanych w cenniku.")
waluta = input()
wybor(waluta)
