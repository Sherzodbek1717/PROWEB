# input() - funksiyasi

# name = input("Ismingizni kiriting: ")
# print('Salom', name)

# print("Ma'lumotlarni to'ldiring👇")
# name = input("Ismingizni kiriting: ")
# job = input("Kasbingingizni kiriting: ")
# age = input("Yoshingizni kiriting: ")
#
# user_full_name = f"Foydalanuvchi: {name}," \
#                  f"kasbi: {job}," \
#                  f"yoshi: {age}"
# print(user_full_name)


# num1 = int(input("1-sonni kiriting: "))
# num2 = int(input("2-sonni kiriting: "))
#
# print(num1 + num2)


# -------------------------------------------------------------
# Solishtirish operatorlari

# >, <, >=, <=, ==, !=

# a = 5
# b = 10
# c = 15
#
# print(a > b)
# print(a < b)
# print(a < c > b)
# print(c >= b)
# print(a <= b)
#
# print(a == b)
# print(a != b)

# Harflarni solishtirish

# print('a' > 'b')
# print('b' > 'c')
# print('C' > 'c')

# print('ab' < 'abc')
# print('abc' > 'abCde')

# -------------------------------------------------------------
# ord() - funksiyasi
# print(ord('a'))

# -------------------------------------------------------------
# chr() - funksiyasi
# print(chr(97))

# word = 'hELlo wOrlD'
#
# print(word.title())
# print(word.capitalize())
# print(word.upper())
# print(word.lower())


# -------------------------------------------------------------
# Shart operatori. if, elif, else konstruksiyasi

#
# if shart1:
#     kodi qismi
# elif shart2:
#     kod qismi
# elif shart3:
#     kod qismi
# else:
#     kod qismi


# a = 15
# b = 10
#
# if a > b:
#     print("birinchi son katta")
# elif b > a:
#     print("ikkinchi son katta")
# else:
#     print("sonlar o'zaro teng")


# name = input("Ismingizni kiriting: ")
#
# if name == 'Abror':
#     message = 'Salom Abror'
# elif name == 'Toxir':
#     message = 'Salom Toxir'
# else:
#     message = 'Bunday ismini bilmayman😐'
#
# print(message)


# -------------------------------------------------------------
# and, or, not operatorlari

name = input("Ismingizni kiriting: ").capitalize()
password = input('Parolni kiriting: ')

if not name and not password:
    message = 'Ism va parolni kiritmadingiz!'
elif not name:
    message = "Ismni kirtimadingiz!"
elif not password:
    message = 'Parolni kiritmadingiz!'

elif (name == 'Abror' and password == '123') or (name == 'Toxir' and password == '1'):
    message = f'Siz foydalanuvchisiz'

elif (name == 'Sobit' and password == 'abv') or (name == 'Botir' and password == '456'):
    message = 'Siz adminsiz'
else:
    message = 'Ism yoki parol noto\'g\'ri'
print(message)