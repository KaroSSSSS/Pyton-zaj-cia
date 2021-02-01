import datetime 
import calendar
weekdays = ["Poniedziałek", "Wtorek", "Środa",  
           "Czwartek", "Piątek", "Sobota", "Niedziela"] 
def urodzinki(bday): 
  
    # Dzieli date na rok miesiąc i dzień, oddzielone myślnikiem
    year, month, day = bday.split('-')
    return year, month, day 
def get_birthday(birthday): 
  
    year, month, day = urodzinki(bday)
  
    bdate = datetime.datetime(int(year), int(month), int(day)) 
  
    weekday = bdate.weekday() 
  
    day = weekdays[weekday] 
  
    print(day)


def dzis_jutro_wczoraj():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days = 1)
    tomorrow = today + datetime.timedelta(days = 1) 
    print("Dziś -",today,"Wczoraj -",yesterday,"Jutro -",tomorrow)
print("Witaj w programie, wybierz jedną z opcji w menu:")
print("1. Data wczoraj, dziś, jutro")
print("2. Kiedy wielkanoc? ") #nie zrobione, nie miałem pomysłu jak to zrobić.
print("3. W który dzień tygodnia się urodziłeś?")
menu = int(input())
if menu == 1:
    dzis_jutro_wczoraj()
elif menu == 3:
    bday = input("Podaj datę w formacie RRRR-MM-DD oddzielone myślnikami")
    get_birthday(bday)
else:
    print("Funkcja nie istnieje, lub nie została zrobiona")