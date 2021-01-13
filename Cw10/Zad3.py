tekst = f"""Długo na szturm i szaniec poglądał w milczeniu. Na
koniec rzekł: 'Stracona'."""
tekst1 = tekst[:(tekst.find(".", 0,len(tekst)))]
print(tekst1)
lista= ["Zwinny", "lis", "przeskoczył", "nad", "leniwym",
"psem", "."]
sent_str = ""
for i in lista:
    sent_str += str(i) + " "
sent_str = sent_str[:-3]
sent_str = sent_str+lista[6]
print(sent_str)