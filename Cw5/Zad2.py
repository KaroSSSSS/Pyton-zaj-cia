from statistics import median
n = int(input("Podaj liczbe"))
x = int(input("Podaj liczbe"))
k = 0
srednia = 0
lista = []
for i in range(n, x+1):
    lista.append(i)
    srednia += i
    if k !=6:
       k +=1
       print(i)
    else:
        continue
    if i == x+1:
        break
print(median(lista))
print(srednia/len(lista))
print(min(lista))
print(max(lista))