tup1 = ("pies", "kot", "foka", "lew", "wąż", "słoń")
for i in tup1:
    s = str(input("Podaj słowo: "))
    if s in tup1:
        print("Szukane słowo jest w krotce")
        print("Jego indeks: ", tup1.index(s))
        break
    else:
        print("Nie ma takiego słowa.")
        break
