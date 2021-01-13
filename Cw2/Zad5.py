alko = int(input("Podaj stosunek zawartości alkoholu we krwi (w promilach):"))
if alko < 0.2:
    print("Jesteś trzeźwy")
elif alko < 0.5:
    print("Jesteś w stanie po zuzyciu alkoholu")
else:
    print("Jesteś pijany")