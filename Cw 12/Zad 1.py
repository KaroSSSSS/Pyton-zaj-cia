import math
x = int(input("Podaj liczbę x: "))
y = int(input("Podaj liczbę y: "))

def suma(x,y):
    suma = x + y
    return suma
def roznica(x,y):
    roznica = x-y
    return roznica
def mnozenie(x,y):
    iloczyn = x * y
    return iloczyn
def dzielenie(x,y):
    if y==0:
        print("PAMIĘTAJ CHOLERO NIE DZIEL PRZEZ ZERO")
    else:
        iloraz = x/y
        return iloraz
def pierwiastek_x(x):
    z = math.sqrt(x)
    return z
def pierwiastek_y(y):
    c = math.sqrt(y)
    return c
print("Suma :", suma(x,y))
print("Różnica :", roznica(x,y))
print("Iloczyn :", mnozenie(x,y))
print("Iloraz: ", dzielenie(x,y))
print("Pierwiastek z x: ", pierwiastek_x(x))
print("Pierwiastek z y: ", pierwiastek_y(y))