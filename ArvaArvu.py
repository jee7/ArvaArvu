import random

arv = random.randint(10, 30)

print("Tere! Mis su nimi on?")
nimi = input()
print("Hei, "+ nimi+ ", Arva ära millist arvu 10 ja 30 vahel ma mõtlen?")
arvamus = int(input())
loendur = 0

while arvamus != arv or loendur < 10:
    if arv > arvamus:
        print ("Liiga väike! Paku suuremat arvu!")
    elif arv < arvamus:
        print ("Liiga suur! Paku väiksemat arvu!")
    arvamus = int(input())
    loendur = loendur + 1

if arvamus == arv:
    print ("Tubli "+nimi+ "! Sa arvasid mu arvu", loendur, "korraga." )
else :
    print ("Viiest arvamisest ei piisanud! Äkki tahad taktikat muuta?")

