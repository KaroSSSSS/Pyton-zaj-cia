a = int(input("Podaj pierwszą liczbę : "))
b = int(input("Podaj drugą liczbę : "))
c = int(input("Podaj trzecią liczbę : "))

if a > b:
    if a > c:
        print("Pierwsza liczba jest największa")
    else:
        print("Trzecia liczba jest największa")
elif b > a:
    if b > c:
        print("Druga liczba jest największa")
    else:
        print("Trzecia liczba jest największa")