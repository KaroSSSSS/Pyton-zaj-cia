MarbleLeague = {
    "Balls of Chaos", 
    "Chocolatiers", 
    "Jawbreakers",
    "Kobalts", 
    "Limers", 
    "Mellow Yellow", 
    "Oceanics",
    "O'rangers", 
    "Pinkies", 
    "Rojo Rollers"
}
MarbleLeague2 = { 
    "Savage Speeders", 
    "Snowballs", 
    "Team Galactic", 
    "Team Momo", 
    "Team Primary", 
    "Limers", 
    "Jungle Jumpers", 
    "Midnight Wisps", 
    "Quicksilvers", 
    "Shining Swarm"
    }
MarbleLeague3 = {
    "Crazy Cat's Eyes",
    "Hazers",
    "Minty Maniacs",
    "Raspberry Racers",
    "Team Momary",
    "Green Ducks",
    "Indigo Stars",
    "Limers",
    "Hornets",
    "O'Rangers"
}
MarbleLeague4 = {
    "Raspberry Racers",
    "Rojo Rollers",
    "Savage Speeders", 
    "Snowballs", 
    "Team Galactic", 
    "Limers",
    "Balls of Chaos", 
    "Chocolatiers", 
    "Jawbreakers",
    "Kobalts", 
}
intersection = MarbleLeague.intersection(MarbleLeague2,MarbleLeague3,MarbleLeague4)
print("Intersection lul")
print(intersection)
difference = MarbleLeague.difference(MarbleLeague2,MarbleLeague3,MarbleLeague4)
print("Difference")
print(difference)
Onio = MarbleLeague.union(MarbleLeague2,MarbleLeague3,MarbleLeague4)
print("A GOOD ONIO IS A HEVI ONIO(union)")
print(Onio)
upperset1= MarbleLeague.issuperset(MarbleLeague2)
print(upperset1)
upperset2= MarbleLeague3.issuperset(MarbleLeague4)
print(upperset2)
#uppersetFINALLE = upperset1.issuperset(upperset2) Poprzednie zwracają FALSE
print("Issuperset")
#print(uppersetFINALLE) 
print("issubset")
issubset1 = MarbleLeague.issubset(MarbleLeague2)
print(issubset1)
issubset2 = MarbleLeague3.issubset(MarbleLeague4)
print(issubset2)
#issubsetFINALLE = issubset1.issubset(issubset2)
#print(issubsetFINALLE)
print("intersection")
print(len(intersection))
print("difference")
print(len(difference))
print("ONIO")
print(len(Onio))
print("issuperset nie ma długości bo typ bool")
#print(len(upperset1)) 
###print(len(upperset2))
print("issubset nie ma długości bo typ bool")
#print(len(issubset1))
#print(len(issubset2))
print(MarbleLeague-intersection)
print(MarbleLeague2-intersection)
print(MarbleLeague3-intersection)
print(MarbleLeague4-intersection)

MarbleLeague_list = list(MarbleLeague)
print(MarbleLeague_list)
MarbleLeague2_list = list(MarbleLeague2)
print(MarbleLeague2_list)
MarbleLeague3_list = list(MarbleLeague3)
print(MarbleLeague3_list)
MarbleLeague4_list = list(MarbleLeague4)
print(MarbleLeague4_list)
# set nie może mieć powtarzających się wartości, a lista może mieć :)
# można w listach sortować dane, w setach nie
# w listach można edytować dane