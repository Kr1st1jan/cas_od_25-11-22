#           #0      #1    #2
# osoba = ["Marko", 25, "iOS"]
# print(osoba)

# print(osoba[0])
# print(osoba[1])
# print(osoba[2])

#range 

# for broj in range(5):
#     print(broj)
# print()

# for broj in range(5, 20):
#     print(broj)
# print()

# for broj in range(0, 31, 2):
#     print(broj)


# kurs= "Pytnon"
# # print(kurs[0])
# # print(kurs[1])
# # print(kurs[2])
# # print(kurs[3])
# # print(kurs[4])
# # print(kurs[5])

# print(len(kurs)) #Komanda len nam sluzi za prebrojavanje slova u recima

#                #0,1,2,3,4,5
# for indeks in range(0, len(kurs)-1):
#     print(kurs[indeks])


# ustanova = "IT Academy"
# print(len(ustanova))

# for slovo in range(len(ustanova)-1):
#     print(ustanova[slovo])

# '''
#     for brojac in sekvenca:
#         ...
# '''

# for slovo in ustanova:
#     print(slovo)

#String format nije mutabilan sto znaci da ne moze da se menja

# tip_korisnika = "admin"
# tip_korisnika[0] = "A"


# korisnicko_ime = input("Unesite Korisnicko Ime: ")

# if korisnicko_ime.lower() == "admin1":
#     # lower komanda pretvara sve u mala slova AdmiN1 -> admin1 ; dok upper pretvara sva slova u velika admin1 -> ADMIN1
#     print("Dobrodosli !")
# else:
#     print("Neispravni Podaci")


# tekst = "A*B#*C#D"

# for slovo in tekst:
#     if slovo != "*" and slovo != "#":
#         print(slovo)
# # indeks
# for x in range(len(tekst)-1):
#     if tekst[x] == "*":
#         print("* je na poziciji: ", x)
#     elif tekst[x] == "#":
#         print("# je na poziciji: ", x)
#     else:
#         print(tekst[x])

# slovo = "A"
# print(slovo in tekst)

# LISTA

# telefoni = ["iPhone 11", "Samsung A22", "iPhone 14", "Huawei Mate 50"]

# print(telefoni[1])

# telefoni[0] = "iPhone 12 Pro"

# print(telefoni[0])


# # PONUDA TELEFONA

# for telefon in telefoni:
#     print(telefon)

# for indeks in range(len(telefoni)-1):
#     # print(indeks)
#     print(telefoni[indeks])


# # sve dok je broj indeksa manji od rednog broja poslednjeg clana

# indeks = 0
# duzina_lisete = len(telefoni) #4
#                     #4
# while indeks < duzina_lisete:
#     print(telefoni[indeks])
#     indeks += 1


# ponuda_smerova = ["Python", "PHP", "iOS", "Java"]
# zeljeni_smer = input("Unesite zeljeni smer: ")

# for smer in ponuda_smerova:
#     if zeljeni_smer == smer:
#         print("Ovaj smer je dostupan. Upisao si se!")
#         break
#     else:
#         print("Niste uneli neki od ponudjenih smerova")


# ponuda_smerova = ["Python", "PHP", "iOS", "Java"]
# ponuda_smerova.append("c#")


# print(ponuda_smerova)

# proba = []
# proba.append(5)
# proba.append("Hello")
# print(proba)

# # proba.clear()    #Uklanja sve
# # proba.remove(5)  #Uklanja tu vrednost
# # proba.pop(0)     #Uklanja vrednost na tom indeksu
# # del proba[0]     #Uklanja vrednost na tom indeksu

# print(proba)

#               #0       #1       #2
# laptopovi = ["Acer", "Dell", "MacBook"]
#              # Od 0 do 3
# for i in range(len(laptopovi)):
#     print(laptopovi[i])



# for vrednost in laptopovi:
#     print(vrednost)


# # i - indeks
# # v - vrednost

# for i, v in enumerate(laptopovi):
#     print("Indeks:", i, "Vrednost:", v)


# termini = ["Ponedeljak", "Sreda", "Petak"]

# for x in range(len(termini)):
#     if "Utorak" == termini[x]:
#         print("Dodajte i Utorak u spisak.")
#     print(termini[x])

# if "Utorak" in termini:
#     print("Utorak je medju terminima.")
# else:
#     print("Dodajte i Utorak u spisak.")


# # if not "Utorak" in termini: da li se ne nalazi


# smerovi = ["Python", "PHP", "iOS", "Java", "C#", "Frontend", "Android"]

# promocija = smerovi[1:4:2]
# print(promocija)


# korisnici = ["Petar", "Marija", "Jovana", "Vladimir", "Milos", "Katarina"]

# pobednici = korisnici[0:3]
# print(pobednici)
# pobednici.clear()

# for i in range(len(korisnici)):
#     if i == 0 or i == 1 or i == 2:
#         pobednici.append(korisnici[i])


#VEZBA

# brojevi = [ 1, 10, 7, 2, 6, 3, 17, 30]

# parni = []
# neparni = []

# # for petlja
# # if else
# # % 2 == 0
# # append

# for broj in brojevi:
#     # parni.append(broj) if broj % 2 == 0 else neparni.append(broj)
    
#     if broj % 2 == 0:
#         parni.append(broj)
#     else:
#         neparni.append(broj)

# print("Parni", parni)
# print("Neparni", neparni)



# rec = input("Unesite Rec za Proveru: ")
# pocetni_indeks = 0
# krajnji_indeks = len(rec)-1
# palindrom = True

# while pocetni_indeks < krajnji_indeks:
#     if rec[pocetni_indeks] != rec[krajnji_indeks]:
#         print("Nije Palindrom")
#         palindrom = False
#         break
#     pocetni_indeks += 1
#     krajnji_indeks -= 1
# else:
#     print("Jeste Palindrom")

# print("Rec", rec, ("jeste" if palindrom else "nije") , "palindrom")


kursevi = ["Python", "iOS", "Desing"]

# Unos kursa putem inputa
# provera da li postoji u listi kurseva (in)
# append
# svaki put nakon unosa ili poruke ispisati listu kurseva
while True:
    unet_kurs = input("Unesite Kurs: ")

    if unet_kurs == kursevi:
        print("Kurs Postoji.", kursevi)
    else:
        kursevi.append(unet_kurs)
    print(kursevi)
            
            
        