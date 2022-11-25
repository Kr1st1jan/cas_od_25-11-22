pozicija_automobila = 0
pozicija_cilja = 10

# pozicija_automobila += 2
# print(pozicija_automobila >= pozicija_cilja)
# pozicija_automobila += 2
# print(pozicija_automobila >= pozicija_cilja)
# pozicija_automobila += 2
# print(pozicija_automobila >= pozicija_cilja)
# pozicija_automobila += 2
# print(pozicija_automobila >= pozicija_cilja)
# pozicija_automobila += 2
# print(pozicija_automobila >= pozicija_cilja)


# for pozicija in range(0, 5):
#     pozicija_automobila += 2
#     print(pozicija_automobila >= pozicija_cilja)



#For petlja 

# for sledeci in ["Mile", "Jovana","Petar", "Marija", 1, 5, 7, 9]:
#     print("Hello", sledeci)

# print("For Petlja se zavrsila")



# for brojac in range(1, 101, 5): 
#     print("Hello...", brojac)



#Vezba 1

# start_Date = 2012
# end_Date = 2015

# print("******* Allowed Years ********")

# for date in range(start_Date , end_Date+1):
#     print(date, end=", ") #Ovo end=", " se postavlja da bi poredjali brojeve u jednom redu

# print("******************************")

zeljeni_broj = int(input("Unesite broj: "))

print("1\t2\t3") #Ovo \t sluzi kao komanda TAB, da odvoji brojeve

print("------------------")

for broj in range(1, zeljeni_broj+1):
    print(broj * 1, end="\t")
    print(broj * 2, end="\t")
    print(broj * 3)





#odstampaj samo parne brojeve iz opsega 1 do 100

# for broj in range(0, 101, 2):
#     print(broj)


# for broj in range(1, 101):
#     if broj % 2 == 0:
#         print(broj)
#     else:
#         print("Neparan broj")


# for x in range(10):
#     print("Ovo je X", x)
#     for y in range(10):
#         print("Ovo je Y", y)



'''
    # # # # #
    # # # # #      
    # # # # #      
    # # # # #
'''

# # vrednost = "..." if uslov else "..."
# for x in range(5):
#     for y in range(5):
#         print("*" if x == y else "#", end=" ")
#         # if x == y:
#         #     print("*", end=" ")
#         # else:
#         #     print("#", end=" ")
#     print("")



# visina = 10
# sirina = 1
# for x in range(visina):
#     for y in range(x):
#         print("*", end=" ")
#     sirina += 1
#     print()


'''
    # # # # # #
    #         #
    #         #      
    #         #      
    # # # # # #
'''



# for x in range(10):
#     for y in range(10):
#         if x == 0 or x == 9 or y == 0 or y == 9:
#             print("#", end=" ")
#         else:
#             print(" ", end=" ")
#     print()
    