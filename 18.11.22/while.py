import random
# sekunde = 10

#     #True / False
# while sekunde > 0:
#     #Ovo dole se izvrsava ako je True
#     print(sekunde)
#     sekunde -= 1 # =9 ,8, 7, 6, 5, 4, 3, 2, 1, 0



# while False:
#     print("Cao")


#Baterija


# baterija = 90
# while baterija > 0:
#     print("Mozete koristiti uredjaj, procenat baterije: ", baterija, "%")
#     baterija -= random.randint(5, 15)

# print("Baterija je prazna...")



# zivoti = 5
# while zivoti > 0:
#     print("Igra je u toku... Vas broj zivota:", zivoti)
#     zivoti -= 1

# print("Igra je zavrsena... Broj zivota:", zivoti)


# for zivot in range(5, 0, -1):
#     print("Igra Traje...")

# print("Igra je zavrsena...")


# broj_pokusaja = 7
# poeni = 0

# while broj_pokusaja > 0:
#     srecan_broj = random.randint(1, 20)
#     moj_broj = int(input("Unesite Broj: "))
    
#     if srecan_broj == moj_broj:
#         print("Pogodak! Moj Broj:", moj_broj, "Srecan Broj:", srecan_broj)
#         poeni += 1
#         break
    
#     else:
#         print("Promasaj! Moj Broj:", moj_broj, "Srecan Broj:", srecan_broj)
#         broj_pokusaja -= 1

# print("Igra je zavrsena... Vas broj poena:", poeni)



for broj in range(1, 10):
    print(broj)
    if broj == 5:
        break


#Continue
#Stampaj sve osim 3
for broj in range(1, 10):
    if broj == 3:
        continue
    print(broj)



for ime in ["Petar", "Marko", "Jovana", "Katarina"]:
    if ime == "Milica":
        print("Pronadjen/a!")
        break
    print(ime)
else:
    print("Zavrseno citanje polaznika...")

print("Ovo se izvrsava u svakom slucaju")




zbir = 0


while True:
    broj = input("Unesite broj: ")

    if broj == "":
        print("Zbir je: ", zbir)
    elif broj.isnumeric():
        zbir += int(broj)
    elif broj == "quit":
        exit(0)
    else:
        print("Proverite unos.")
        