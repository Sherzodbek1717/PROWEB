# Fayllar bn ishlash

# file = open('byron.txt')
# content = file.read()
# print(content)


# file_ = open('pushkin.txt', encoding='utf-8')
# content = file_.read()
# print(file_)

# ----------------------------------------------------------------------

# 'r' ---> read() - O'qish
# 'w' ---> read() - Yozish
# 'a' ---> append() - qo'shish
# 'wb' ---> write bytes - Yozish
# 'rb' ---> read bytes - Oqish


# file_ = open('pushkin.txt', mode='r', encoding='utf-8')
# print(file_)

# myStr = "Hello World\n"
#
# file = open('test.txt', mode='a', encoding='utf-8')
# file.write(myStr)
# file.close()
#
# while True:
#     name = input("Ism: ")
#     if name == 'stop':
#         break
#     file = open('names.txt', mode='a', encoding='utf-8')
#     file.write(name + '\n')
#     file.close()

# ----------------------------------------------------------------------

# pushkin_file = open('pushkin.txt', mode='r', encoding='utf-8')
# copy_pushkin_file = open('copy_pushkin.txt', mode='w', encoding='utf-8')
#
# content = pushkin_file.read()
# copy_pushkin_file.write(content)
#
# pushkin_file.close()
# copy_pushkin_file.close()
# ----------------------------------------------------------------------

# with open('byron.txt', mode='r', encoding='utf-8') as file:
#     byron_copy = open('byron_copy.txt', mode='w', encoding='utf-8')
#     content = file.read()
#     byron_copy.write(content)
#     byron_copy.close()
#
# print(file.closed)
# print(byron_copy.closed)

#----------------------------------------------------------------------

# file = open('nature.jpg', mode='rb')
# content = file.read()
#
# for i in range(1, 11):
#     copy_image = open(f'images/nature_copy_{i}.jpg', mode='wb')
#     copy_image.write(content)
#     copy_image.close()
#
# file.close()


#----------------------------------------------------------------------
#amaliyot

i = 1
while True:
    name = input ("Ism: ")
    if name == 'stop':
        break
    lastname = input("Familiya: ")
    age = int(input("Yosh: "))
    address = input("Manzil: ")

    text = f'''ID:{i}
Lastname: {lastname}
Age: {age}
Address: {address}\n'''

    file = open('user_info.txt', mode='a', encoding='utf-8')
    file.write(text)
    file.close()
    i += 1
    print('-' * 100)

