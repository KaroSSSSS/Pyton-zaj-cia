a = int(input("Podaj pierwszą liczbę : "))
b = int(input("Podaj drugą liczbę : "))
c = int(input("Podaj trzecią liczbę : "))
d = int(input("Podaj czwartą liczbę: "))

if a > b and a > c and a > d:
    print("Pierwsza liczba jest największa")
elif b > a and b > c and b > d:
    print("Druga liczba jest największa")
elif c > a and c > b and c > d:
    print("Trzecia liczba jest największa")
else:
    print("Czwarta liczba jest największa")