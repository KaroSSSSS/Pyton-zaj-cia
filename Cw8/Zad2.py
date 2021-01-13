slownik={}
i=0
while i != 10:
    klucz=input("podaj nazwe ")
    wartosc=input("podaj numer ")
    slownik[klucz]=wartosc
    i+=1
print(slownik)
numer1 = list(slownik.values())[0]
numer2 = list(slownik.values())[len(slownik)-1]
print(numer1)
print(numer2)
del slownik[list(slownik)[0]]
del slownik[list(slownik)[len(slownik)-1]]
slownik['new_first_key']= numer1
slownik['new_last_key']= numer2
print(slownik)
del slownik[list(slownik)[4]]
del slownik[list(slownik)[5]]
print(slownik)
slownik.clear()
slownik[input("podaj nazwe kontaktu")]= input("podaj numer kontaktu")
slownik[input("podaj nazwe kontaktu")]= input("podaj numer kontaktu")