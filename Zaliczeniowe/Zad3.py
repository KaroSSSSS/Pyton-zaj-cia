import time

wynik = 0

def pytanie_1():
    global wynik
    print("Liczba 1000101 w zapisie binarnym to ile w zapisie dziesiętnym?")
    odpowiedz1 = int(input("Odpowiedź :"))
    if odpowiedz1 == 69:
        print("Nice! Dobra odpowiedź!")
        wynik == wynik +1
    else:
        print("Zła odpowiedź! Poprawna : 69")
    time.sleep(2)

def pytanie_2():
    global wynik
    print("Ile bitów mieści się w bajcie?")
    odpowiedz2 = int(input("Odpowiedź :"))
    if odpowiedz2 == 8:
        print("Nice! Dobra odpowiedź!")
        wynik += 1
    else:
        print("Zła odpowiedź! Poprawna: 8")
    time.sleep(2)

def pytanie_3():
    global wynik
    print("Ile Gigabajtów to jeden Terabajt? (Jednostek komputerowych, a nie oszukujących sklepowych)")
    odpowiedz3 = int(input("Odpowiedź :"))
    if odpowiedz3 == 1024:
        print("Nice! Dobra odpowiedź!")
        wynik += 1
    else:
        print("Zła odpowiedź! Poprawna : 1024")
    time.sleep(2)

def pytanie_4():
    global wynik
    print("Czy Python jest językiem kompilowanym? (Tak / Nie)")
    odpowiedz4 = input("Odpowiedź :")
    if odpowiedz4 == "Nie" or odpowiedz4 == "nie":
        print("Nice! Dobra odpowiedź!")
        wynik += 1
    else:
        print("Zła odpowiedź! Poprawna: Nie")
    time.sleep(2)

def pytanie_5():
    global wynik
    print("Czy pamięć RAM DDR3 pracuje na 1,2 V? (Tak / Nie)")
    odpowiedz5 = input("Odpowiedź :")
    if odpowiedz5 == "Nie" or odpowiedz5 == "nie":
        print("Nice! Dobra odpowiedź!")
        wynik += 1
    else:
        print("Zła odpowiedź! Poprawna: Nie")
    time.sleep(2)

def pytanie_6():
    global wynik
    print("Jakiego separatora instrukcji używa język c++?")
    odpowiedz6 = input("Odpowiedź :")
    if odpowiedz6 == ";":
        print("Nice! Dobra odpowiedź!")
        wynik += 1
    else:
        print("Zła odpowiedź! Poprawna: ;")
    time.sleep(2)

def pytanie_7():
    global wynik
    print("Dzisiejsze systemy pracują na architekturze x64 i ... ? (Odpowiedź podaj w formacie x## gdzie ## to liczba)")
    odpowiedz7 = input("Odpowiedź :")
    if odpowiedz7 =="x86":
        print("Nice! Dobra odpowiedź!")
        wynik += 1
    else:
        print("Zła odpowiedź! Poprawna: x86")
    time.sleep(2)

def pytanie_8():
    global wynik
    print("Jakiego rodzaju pamięci GDDR używają najnowsze karty RTX 30xx?")
    odpowiedz8 = input("Odpowiedź :")
    if odpowiedz8 == "6" or odpowiedz8 == "GDDR6" or odpowiedz8 =="gddr6":
        print("Nice! Dobra odpowiedź!")
        wynik += 1
    else:
        print("Zła odpowiedź! Poprawna: 6 albo GDDR6")
    time.sleep(2)

def pytanie_9():
    global wynik
    print("Który przewód z rodziny RJ używany jest do przesyłania danych router <=> komputer?")
    odpowiedz9 = input("Odpowiedź :")
    if odpowiedz9 == "45" or odpowiedz9 =="RJ45" or odpowiedz9 == "RJ-45" or odpowiedz9 == "rj45" or odpowiedz9 == "rj-45":
        print("Nice! Dobra odpowiedź!")
        wynik += 1
    else:
        print("Zła odpowiedź! Poprawna: RJ-45")
    time.sleep(2)

def pytanie_10():
    global wynik
    print("Czy system ósemkowy używa cyfry 8?")
    odpowiedz10 = input("Odpowiedź :")
    if odpowiedz10 == "Nie" or odpowiedz10 == "nie":
        print("Nice! Dobra odpowiedź!")
        wynik += 1
    else:
        print("Zła odpowiedź! Poprawna: Nie")
    time.sleep(2)
print("Witaj w moim teście! Teraz to masz przerąbane. Poddam Cię 10 pytaniom, na które musisz mi odpowiedzieć.")
time.sleep(3)
print("Kategoria : informatyka")
time.sleep(1)
print("Pytanie pierwsze!")
pytanie_1()
print("Pytanie drugie!")
pytanie_2()
print("Pytanie trzecie!")
pytanie_3()
print("Pytanie czwarte!")
pytanie_4()
print("Pytanie piąte!")
pytanie_5()
print("Pytanie szóste!")
pytanie_6()
print("Pytanie siódme!")
pytanie_7()
print("Pytanie ósme")
pytanie_8()
print("Pytanie dziewiąte!")
pytanie_9()
print("Ostatnie pytanie!")
pytanie_10()
print("Ukończyłeś test! Daj mi teraz chwilkę, abym przeliczył twój wynik!")
time.sleep(5)
if wynik == 10:
    print("Gratulacje! Osiągnąłeś maksymalną liczbę pkt! Ocena: 5")
elif wynik >=7:
    print("Nieźle! Osiągnąłeś ",wynik," punktów! Ocena: 4")
elif wynik >=5:
    print("Na styk! Osiągnąłeś ",wynik," punktów! Ocena: 3")
else:
    print("Nie udało Ci się, musisz osiągnąć większą wiedzę w kategorii informatyka!")
time.sleep(2)
print("Dziękuję, za udział w teście!")
