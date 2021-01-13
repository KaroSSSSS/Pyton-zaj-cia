import random
q = 0
tablica = []
for i in range(0,6):
    x = int(input("podaj liczbe: "))
    tablica.append(x)
for z in range(0,6):
    p = random.randint(0,49)
    if p in tablica:
        q = q+1
print("trafiles",q,"liczb")