print("Podaj co chcesz przekonwertować? (GB, TB)") # Nie wiem czy jest sens podawać inne rozmiary, bo tylko te w sumie są najczęściej używane. Chyba  ze ktoś chce sobie dyskietki przekonwertować to no.
typ = input()
pojemnosc = int(input("Podaj ile?"))

def GB_rzeczywista(pojemnosc):
    pojemnosc_rzeczywista_GB = (((pojemnosc *1000 *1000 * 1000 )/1024)/1024)/1024
    print("Tyle masz pojemności rzeczywistej",pojemnosc_rzeczywista_GB," GB")

def TB_rzeczywista(pojemnosc):
    pojemnosc_rzeczywista_TB = ((((pojemnosc *1000 *1000 * 1000 *1000 )/1024)/1024)/1024)/1024
    print("Tyle masz pojemności rzeczywistej",pojemnosc_rzeczywista_TB," TB")

if typ =="GB":
    GB_rzeczywista(pojemnosc)
if typ =="TB":
    TB_rzeczywista(pojemnosc)
# Ludzie korzystają z systemu dziesiętnego, którego podstawą jest liczba 10. 
# Natomiast komputery pracują w oparciu o system binarny, czyli dwójkowy, w którym podstawą jest liczba 2. 
# Najmniejszą jednostką pamięci, stosowaną w informatyce jest bajt. 
# Wykorzystywane powszechnie przedrostki dziesiętne (z układu SI) to kilo (k) dla tysiąca, mega (M) dla miliona, giga (G) dla miliarda oraz tera (T) dla biliona. 
# Otrzymujemy więc kolejno kilobajt (tysiąc bajtów), megabajt (milion bajtów), gigabajt (miliard bajtów) oraz terabajt (bilion bajtów).
# Dlatego według producentów, dysk SSD o pojemności 512 GB ma pojemność dokładnie 512 000 000 000 bajtów (512 bajtów x 1000 x 1000 x 1000).
# Jednak w przypadku komputerów i wykorzystywanego przez nich systemu dwójkowego, obliczanie tych wartości wygląda nieco inaczej. 1 kilobajt równa się 1024 bajtom. 
# 1 megabajt to z kolei 1048576 bajtów (1024 x 1024), a 1 gigabajt to 1073731824 bajty (1024 x 1024 x 1024).