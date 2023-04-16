# Hatoliklar bilan ishlash

# try: ---> urinib ko'r
# except ---> ...dan tashqari

# list1 = [1, 2, 3]
#     list1[9]

# -------------------------------------------------------------------

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

# -------------------------------------------------------------------
# try:
#     20/0
#     print(name)
#     list1 = [1, 2, 3]
#     list1[10]
# except NameError:
#     print("Xatolik yuz berdi")
# except IndexError:
#     print("Xatolik yuz berdi")
# except ZeroDivisionError:
#     print("Nolga bolish mumkn emas")


# try:
#     print(name)
# except NameError as n:
#     n.__str__ = 'Xatolik!!!'
#     print(NameError.__name__)
#     print(NameError.__doc__)
#     print(n)
#     print(n.__str__)

# -------------------------------------------------------------------
# amaliyot

# while True:
#     user_num = input("Sonni kiring: ")
#     if user_num == 'stop':
#         break
#
#     try:
#         int_num = int(user_num)
#         if int_num == 1:
#             try:
#                 print(name)
#             except NameError:
#                 print("name Mavjud emas")
#         elif int_num == 2:
#             try:
#                 a = tuple()
#                 a.append('b')
#             except AttributeError as ae:
#                 print(ae.__str__())
#         elif int_num == 3:
#             try:
#                 file = open('test.txt')
#                 print(file)
#             except FileNotFoundError:
#                 print(FileNotFoundError.__name__)
#
#     except ValueError as ve:
#         print("Butun son kiriting!!!")
# -------------------------------------------------------------------
# parol yasaw

# from string import ascii_letters, digits
# from random import choice
#
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
# password_string = ascii_letters + punctuation + digits
#
# len_password = input("Parolni nechaxona uzunligida generatsiya qilw kerak: ")
# try:
#     len_password = int(len_password)
#     full_password = ''
#     for i in range(1, len_password + 1):
#         full_password += choice(password_string)
#
#     print(full_password)
# except ValueError:
#     print("Son kiriting: ")

# import string
#
#
# def validate_name(name):
#     for letter in name:
#         if letter in string.punctuation or letter in string.digits:
#             return False
#         else:
#             return True
#
#
# def validate_mail(mail):
#     if '@' in mail and '.' in mail:
#         return True
#     else:
#         return False
#
#
# def validate_age(age):
#     try:
#         if 17 < int(age) < 99:
#             return True
#         else:
#             return False
#     except ValueError:
#         return False
#
#
# with open('registrations.txt', mode='r', encoding='utf-8') as file:
#     good = open('good.txt', mode='w', encoding='utf-8')
#     bad = open('bad.txt', mode='w', encoding='utf-8')
#
#     for line in file:
#         if len(line.split(' ')) != 3:
#             bad.write(line)
#         else:
#             data = line.split(' ')
#             name = validate_name(data[0])
#             mail = validate_mail(data[1])
#             age = validate_age(data[2])
#
#             if name and mail and age:
#                 good.write(line)
#             else:
#                 bad.write(line)
#     good.close()
#     bad.close()
#


#
# try:
#     list1 = [1, 2, 3]
#     list1[10]
#     print(name)
#     20/0
# except Exception as e:
#     print(e.__class__.__name__)






































