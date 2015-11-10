import random

arv = random.randint(1, 999)

print("Tere! Mis su nimi on?")
nimi = input()
print("Hei, "+ nimi+ ", Arva ära millist tuhandest väiksemat arvu ma mõtlen?")
arvamus = int(input())
loendur = 1

while arvamus != arv :
    if arv > arvamus:
        print ("Liiga väike! Paku suuremat arvu!")
    elif arv < arvamus:
        print ("Liiga suur! Paku väiksemat arvu!")
    arvamus = int(input())
    loendur = loendur + 1
    if loendur > 10:
        break

if loendur <= 10:
    print ("Tubli "+nimi+ "! Sa arvasid mu arvu", loendur, "korraga." )
else :
    print ("Viiest arvamisest ei piisanud! Äkki tahad taktikat muuta?")

