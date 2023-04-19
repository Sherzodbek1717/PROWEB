# ismlar = ['Abror', 'Toxir', 'Sobir', 'Bakir', 'Jalil', 'Zafar']
#
# for ism in ismlar:
#     if ism == 'Zafar':
#         break
#     elif ism == 'Toxir':
#         continue
#     print(ism.upper())
# else:
#     print('1-else ishlayapti')

# --------------------------------------------------------

# row = 6
# for i in range(6):
#     for j in range(i):
#         print(j, end=' ')
#     print('--------')


# for i in range(1, 10):
#     for j in range(1, 11):
#         print(f"{j} * {i} = {i*j}", end='  ')
#     print('')


# --------------------------------------------------------
# Inkrement

# s = 0
# for i in range(10):
#     # s = s + 1
#     s += 1
#     print(s)


# --------------------------------------------------------
# Dekrement

# s = 10
# for i in range(10):
#     # s = s - 1
#     s -= 1
#     print(s)


# --------------------------------------------------------
# while sikl operatori

# s = 0
# while s < 10:
#     print('Hello', s)
#     s += 1



# while True:
#     print("Hello")
#


products = []
while True:
    user_text = input("Komanda va mahsulot nomini kiriting: ")

    if user_text == 'stop':
        print("Dastur to'xtadi!!!")
        break

    if len(user_text.split(' ')) == 2:
        command, product = user_text.split(' ')
        if command == 'add':
            if product in products:
                print(f"{product} ro'yxatda mavjud! {products}")
            else:
                products.append(product)
                print(f"{product} ro'yxatga qo'shildi! {products}")
        elif command == 'delete':
            pass

    else:
        print("Nimadir xato ketdi!")
