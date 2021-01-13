n = int(input("Podaj ile kolejnych potęg naturalnych liczby 2 mam wyświetlić? :"))
i = 0
wynik = 1
if n == 0:
    print("1")
while i != n:
    wynik =  wynik * 2
    i = i+1
    print(wynik)