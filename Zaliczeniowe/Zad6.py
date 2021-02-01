celsjusz = float(input("Podaj temperaturę w celsjuszach: "))
fahrenheit = (celsjusz * 9/5) + 32
if fahrenheit <= 32:
    print(celsjusz," stopni celsjusza wynosi ",fahrenheit,"farhenheita.")
    print("Woda zamarza")
elif fahrenheit >=212:
    print(celsjusz," stopni celsjusza wynosi ",fahrenheit,"farhenheita.")
    print("Woda wrze")
else:
    print(celsjusz," stopni celsjusza wynosi ",fahrenheit,"farhenheita.")

# funkcje

def cel_kel():
    cel = int(input("Podaj temperaturę w Celsjuszach: "))
    kel = cel + 273.15
    return kel

def kel_cel():
    kel = int(input("Podaj temperaturę w Kelwinach"))
    cel = kel - 273.15
    return kel

def fah_kel():
    fah = int(input("Podaj temperaturę w Fahrenheitach"))
    kel = 273.5 + ((fah - 32.0) * (5.0/9.0))
    return kel

def kel_fah():
    kel = int(input("Podaj temperaturę w Kelwinach"))
    fah = kel - 273.5 * ( 9 / 5 ) + 32
    return fah

def cel_new():
    cel = int(input("Podaj temperaturę w Celsjuszach"))
    new = cel * 0.33
    return new

def new_cel():
    new = int(input("Podaj temperaturę w Newtonach"))
    cel = new / 0.33
    return cel

def fahr_new():
    fahr = int(input("Podaj temperaturę w Fahrenheitach"))
    new = ((fahr - 32)/1.8)*0.33
    return new

def new_fah():
    new = int(input("Podaj temperaturę w Newtonach"))
    fah = (((new/0.33)*1.8)+32)
    return fah

def kel_new():
    kel = int(input("Podaj temperaturę w Kelwinach"))
    new = (kel - 273.15)* 0.33
    return new

def new_kel():
    new = int(input("Podaj temperaturę w Newtonach"))
    kel = (new/0.33) +273.15
#menu

print("Oferuję jeszcze przeliczenie temperatury, powiedz tylko na jaką:")
print("1. Celsjusz - Kelwin")
print("2. Kelwin - Celsjusz")
print("3. Farhenheit - Kelwin")
print("4. Kelwin - Fahrenheit")
print("5. Celsjusz - Newton")
print("6. Newton - Celsjusz")
print("7. Fahrenheit - Newton")
print("8. Newton - Fahrenheit")
print("9. Kelwin - Newton")
print("10. Newton - Kelwin")
print("11. Fahrenheit - Celsjusz")
wybor = int(input("Podaj cyfrę: "))
if wybor == 1:
    print("Temperatura w Kelwinach wynosi",cel_kel())
if wybor == 2:
    print("Temperatura w Celsjuszach wynosi",kel_cel())
if wybor == 3:
    print("Temperatura w Kelwinach wynosi",fah_kel())
if wybor == 4:
    print("Temperatura w Fahrenheitach wynosi",kel_fah())
if wybor == 5:
    print("Temperatura w Newtonach wynosi",cel_new())
if wybor == 6:
    print("Temperatura w Newtonach wynosi",new_cel())
if wybor == 7:
    print("Temperatura w Newtonach wynosi", fahr_new())
if wybor == 8:
    print("Temperatura w Fahrenheitach wynosi",new_fah())
if wybor == 9:
    print("Temperatura w Newtonach wynosi",kel_new())
if wybor == 10:
    print("Temperatura w Kelwinach wynosi",new_kel())
if wybor == 11:
    fahrenheit = float(input("Podaj temperaturę w fahrenheitach "))
    celsius = (fahrenheit - 32) * 5/9
    print(fahrenheit,"F to ",celsjusz,"C")