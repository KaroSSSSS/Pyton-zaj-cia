i = int(input("Podaj wartość od której mam zacząć: "))
while i != 0:
    if i %6 == 0 and i%9 == 0:
        print(i,"Ta liczba jest podzielna przez 6 i 9 z danego zakresu")
    i = i-1