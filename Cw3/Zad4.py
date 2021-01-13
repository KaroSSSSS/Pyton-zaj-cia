i = 100
while i != 200:
    if i%2 == 0 and i%6 != 0 and i%5 != 0 and i%11 != 0:
        print(i,"Ta liczba jest parzysta i nie jest podzielna przez 5, 6 i 11 z zakresu 100-200")
    i = i+1