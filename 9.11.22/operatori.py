import random #ovo koristimo da bi nam kasnije program mogao dati nesto na random

kurs = "Python Fundamentals"
print(kurs)

a = 10
b = 5

print("Sabiranje:", a + b)
print("Oduzimanje:", a - b)
print("Mnozenje:", a * b)
print("Deljenje:", a / b)

rez_mnozenja = a * b

print("Rezultat mnozenja:", rez_mnozenja)

rez_deljenja = a / b  #Deljenje automatski stavlja broj u float (Decimalni broj)

print("Rezultet Deljenja:", int(rez_deljenja))

print("Rezultat Deljenja:", float(rez_deljenja))


a = 5
b = 2


print(5 / 2)

print(5 // 2)   #Sa 2 kose crte se broj deli u celi bez obzira da li je prvobitno decimalan, moze da se koristi da zameni int

print(10 // 3)

print(a ** 2)   #Sa 2 zvezdice stepenujemo broj, ako stavimo a ** 2, rezultat ce biti "na kvadrat", ili ti 5 * 5, sto je 25
print(a ** 3)   # 5*5*5 

a = 10 
b = 2


# Koji je ostatak pri deljenju broja 10 sa 2
print(10 % 2)   #Ostatak je 0, sto znaci da je broj paran

a = 9
b = 2

# Koji je ostatak pri deljenju broja 9 sa 2

print (a % b)   #Ostatak je 1, tada znamo da je broj neparan, i ovde dobija samo ostatak pri deljenju

print(-a)   #Dodavanjem minusa ili plusa pored broja, menjamo ih iz pozitivne u negativne i obrnuto


godine = 25

# godine + 1 - ovako ne moze podici broj iznad iz razloga sto nismo pravilno definisali povecanje


godine = godine + 1    #Ovako je ispravno
print(godine)   #Sada su ovde godine = 26

godine += 1   #Ovo je laksa i kraca verzija gornje operacije, sa njom mozemo takodje i da oduzimamo, mnozimo ili delimo
print(godine)

godine *= 2   #Ovde mnozi sa 2 i dodeljuje
print(godine) 
godine * 2    #Ovde samo mnozi ali ne dodeljuje, tako da je bolje raditi sa gornjom operacijom

godine /= 2   #Ovde delimo
print(godine)

#SADA KRECEMO DA RADIMO VEZBE SA INPUTOM (Unosom)

broj1 = 10
broj2 = 5

# print("Prvi broj:", broj1)
# print("Drigi broj:", broj2)

# print("Rezultat:", broj1 + broj2)


# broj1 = input("Unesi prvi broj:  ") #Kada aktiviramo ovu komandu, moramo u konzoli ukucati sta zelimo da stavimo u taj input, ali moramo koristiti input iz razloga sto input sve brojeve stavlja pod navodnike

# "40" -> 40  - MORAMO DA KORISTIMO INT, nebitno da li tokom inputa ili na kraju na printu

# broj2 = input("Unesite drugi broj:  ")

# print("Sabiranje:", int(broj1) + int(broj2))


#Postavljanje vrednosti
# pi = 3.14
# povrsina_kruga = 0

# r = float(input("Unesite r:  "))

# povrsina_kruga = r ** 2 * pi   #Ovo je r na kvadrat pi

# print("Povrsina kruga je:", povrsina_kruga)


#OVDE VEZBAMO >, <, =   - TU SU RESENJA UVEK U TRUE ILI FALSE FORMATU

godine = 15

print(godine > 18)  #Vece u odnosu na broj unet u kutiji
print(godine < 18)  #Manje u odnosu na broj unet u kutiji
print(godine >= 18) #Vece ili Jednako u odnosu na broj unet u kutiji
print(godine <= 18) #Manje ili Jednako u odnosu na broj unet u kutiji

print(godine != 18) #Da li je Razlicito u odnosu na broj unet u kutiji

aktuelan_kurs = "PPF"  #STA NAPISEMO KUTIJI SE MORA TACNO NAPISATI I U PRINTU. DA LI SU MALA ILI VELIKA SLOVA, DA LI JE DOBRO NAPISANO,itd...
print(aktuelan_kurs == "PPF")


# broj = int(input("Unesite Broj:  "))

# ostatak = broj % 2

# print(ostatak == 0) # Ako je ostatak 0 - paran broj


# moj_broj = int(input("Unesite Broj:  "))
# racunar = random.randint(1, 10)

# print("Korisnik:", moj_broj)
# print("Racunar;", racunar)

# print("Pogodak:", moj_broj == racunar)


# automobil_x                                                cilj_x

# automobil_pozicija = 0
# cilj_pozicija = 50

#Ovde pomeramo auto od 0 do 50. Kada je 0 tada je na pocetku, a kada je 50 ili vise onda je stigao ili prosao cilj

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 10
# print(automobil_pozicija >= cilj_pozicija)

# automobil_pozicija += 20
# print(automobil_pozicija >= cilj_pozicija)


# godine = int(input("Koliko imate godina?   "))

# print("Allowed - ", godine >= 13)

uneto_ime = "admin1"
uneta_sifra = "123456"

ime_baza = "admin"
sifra_baza = "12345"

ispravna_sifra = uneta_sifra == sifra_baza   # Ovde gledamo da li je sifra jednaka sa unetom sifrom,  uneta_sifra == sifra_baza 
ispravno_kor_ime = uneto_ime == ime_baza    #Ovde gledamo da li je ime jedanako da unetim imenom, uneto_ime == ime_baza

uspesno_logovanje = ispravna_sifra and ispravno_kor_ime
print(uspesno_logovanje)

'''

and

true true --> true
true false --> false
false true --> false
false false --> false


or

true true --> true
true false --> true
false true --> true
false false --> false
'''


# uneto_ime = "admin"
# uneta_sifra = "123456"

# ime_baza = "admin"
# sifra_baza = "12345"

# ispravna_sifra = uneta_sifra == sifra_baza    #False
# ispravno_kor_ime = uneto_ime == ime_baza      #True

# uspesno_logovanje = ispravna_sifra or ispravno_kor_ime
# print(uspesno_logovanje)


# lepo_vreme = True
# print(not lepo_vreme)

# tamna_tema = True
# print(not tamna_tema)


#VEZBA


smer = input("Smer: ")
generacija = int(input("Generacija: "))

provera_smer = smer == "Python"
provera_generacija = generacija == 2022

konacno = provera_smer and provera_generacija

print("Uspesno:", konacno)


