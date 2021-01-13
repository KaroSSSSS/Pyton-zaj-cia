prevnum = 0
num = 0
suma = 0
k = 0

lista = []
while True:
    num = float(input("Podaj liczbe"))
    lista.append(num)
    if k == 0:
        num = lista[0]
        prevnum = num
        suma = num
        print(suma)
        k += 1
    else:
        num = lista[k]
        if num != prevnum:
            prevnum = num
            suma += num
            print(suma)
            k += 1
        else:
            break