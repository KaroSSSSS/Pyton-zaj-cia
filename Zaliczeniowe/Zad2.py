# Materiały 
# https://poradnikprzedsiebiorcy.pl/-czy-wiesz-ile-wynosi-calkowity-koszt-zatrudnienia-pracownika
emerytalne = 0.0976
rentowe = 0.065
wypadkowe = 0.0167
FP = 0.0245
FGSP = 0.01
placa = int(input("Podaj ile brutto ma zarabiać twój pracownik :"))
emerytalne2 = placa*emerytalne
rentowe2 = placa*rentowe
wypadkowe2 = placa*wypadkowe
fundusz = placa*FP
fundusz2 = placa * FGSP

print("Za emerytalne płacisz : ",round(emerytalne2,2) )
print("Za rentowe płacisz : ", round(rentowe2,2) )
print("Za wypadkowe płacisz : ", round(wypadkowe2,2) )
print("Za fundusz pracy płacisz : ", round(fundusz,2))
print("Za FGŚP, cokolwiek to nie znaczy, płacisz", round(fundusz2,2) )
print("Za całość płacisz : ", round(placa + emerytalne2 + rentowe2 + wypadkowe2 + fundusz+ fundusz2,2))