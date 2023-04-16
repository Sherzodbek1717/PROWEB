# Hatoliklar bilan ishlash

# try: ---> urinib ko'r
# except ---> ...dan tashqari

# list1 = [1, 2, 3]
#     list1[9]

#-------------------------------------------------------------------

# try:
#     print(name)
# except NameError:
#     print("Xatolik yuz berdi")
#
# try:
#     list1 = [1, 2, 3]
#     list1[9]
# except IndexError:
#     print("Ro'yxat Indeksi diapazondan tashqarida")

#-------------------------------------------------------------------
try:
    print(name)
    list1 = [1, 2, 3]
    list1[10]
except NameError:
    print("Xatolik yuz berdi")
except IndexError:
    print("Xatolik yuz berdi")




