menu={}
i=0
while i != 10:
    nazwa_pizzy=input("podaj nazwe pizzy ")
    cena_pizzy=input("podaj cene pizzy ")
    menu[nazwa_pizzy]=cena_pizzy
    i+=1
for k, v in menu.items():
    print(k, v)
del menu[max(menu, value=menu.get)]
del menu[min(menu, value=menu.get)]
print(menu)
nazwa_pizzy=input("podaj nazwe pizzy ")
cena_pizzy=input("podaj cene pizzy ")
menu[nazwa_pizzy]=cena_pizzy
print(menu)