# linki jakie użyłem, do pozyskania procentów do zadania :
# https://poradnikprzedsiebiorcy.pl/-jak-wyliczac-wynagrodzenia
# https://ksiegowosc.infor.pl/podatki/pit/pit/pracownik/724285,Wynagrodzenie-pracownika-obliczenie-podatku-skladek-i-kosztu-pracodawcy.html



# Dane i pobranie wartości płacy
placa = int(input("Podaj ile zarabiasz (brutto) w złotówach :"))
emerytalne = 0.0976
rentowe = 0.015
chorobowe = 0.0245
zdrowotne = 0.09
PIT = 0.17
koszt_przychodu = 111.25
# Obliczenie ile płaci sie na ubezpieczenie emerytalne ze swojej płacy
placisz_emerytalne = emerytalne * placa

print("Tyle płacisz na składkę emerytalną: ", round(placisz_emerytalne,2))
# Obliczenie ile płaci sie na ubezpieczenie rentowe ze swojej płacy
placisz_rentowe = rentowe * placa
print("Tyle płacisz na składkę rentalną: ", round(placisz_rentowe,2))
# Obliczenie ile płaci sie na ubezpieczenie chorobowe ze swojej płacy
placisz_chorobowe = chorobowe * placa
print("Tyle płacisz na składkę chorobową: ", round(placisz_chorobowe,2))
# Obliczenie ile płaci sie na ubezpieczenie zdrowotne ze swojej płacy 
podstawa_wymiaru_zdrowotnej = placa - placisz_rentowe - placisz_emerytalne - placisz_chorobowe
placisz_zdrowotne = podstawa_wymiaru_zdrowotnej * zdrowotne
print("Tyle płacisz na składkę zdrowotną: ", round(placisz_zdrowotne,2))
#Składka zdrowotna do odliczenia do pitu
skladka_pit_zdrowotna = podstawa_wymiaru_zdrowotnej * 0.0775
print("Tyle wynosi składka zdrowotna do odliczenia od pitu: ", round(skladka_pit_zdrowotna,2))
#podstawa do rozliczenia PIT
podstawa_PIT = round(podstawa_wymiaru_zdrowotnej - koszt_przychodu,0)
print("tyle wynosi twoja podstawa do podatku PIT: ", round(podstawa_PIT,2))
# Ile płacisz na PIT
zaliczka_pit = round((PIT * podstawa_PIT) - 46.33 - skladka_pit_zdrowotna,0)
print("Na PIT zapłacisz tyle :", round(zaliczka_pit,2))
# Obliczenie finalnej wypłaty
wyplata = podstawa_wymiaru_zdrowotnej - placisz_zdrowotne - zaliczka_pit
print("A twoja wypłata wyglada tak :", round(wyplata,2))