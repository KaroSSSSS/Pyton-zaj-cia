import math
promien = int(input("Podaj promień kuli: "))
def pole_kuli(promien):
    pole_k = 4 * 3.14 * math.pow(promien,2)
    return pole_k
def obj_kuli(promien):
    obj_k = 4/3 *3.14 * math.pow(promien,3)
    return obj_k
promien_stozka = int(input("Podaj promień podstawy stożka: "))
wysokosc_stozka = int(input("Podaj wysokość stożka: "))
tworzaca_stozka = int(input("Podaj długość tworzącej stożka: "))
def pole_stozka(promien_stozka, tworzaca_stozka):
    pole_st = 3.14 * math.pow(promien_stozka,2) + 3.14 *promien_stozka * tworzaca_stozka
    return pole_st
def obj_stozka(promien_stozka,wysokosc_stozka):
    obj_st = (3.14 * math.pow(promien_stozka,2) * wysokosc_stozka)/3
    return obj_st
krawedz_szescianu = int(input("Podaj długość krawędzi sześcianu: "))
def pole_szescianu(krawedz_szescianu):
    pole_s = 6* math.pow(krawedz_szescianu,2)
    return pole_s
def obj_szescianu(krawedz_szescianu):
    obj_s = math.pow(krawedz_szescianu,3)
    return obj_s
print("Pole kuli wynosi: ", pole_kuli(promien))
print("Objętość kuli wynosi: ", obj_kuli(promien))
print("Pole stożka wynosi: ", pole_stozka(promien_stozka,tworzaca_stozka))
print("Objętość stożka wynosi: ", obj_stozka(promien_stozka, wysokosc_stozka))
print("Pole sześcianu wynosi: ", pole_szescianu(krawedz_szescianu))
print("Objętość sześcianu wynosi: ", obj_szescianu(krawedz_szescianu))