# sonlar = [1, 'ikki', 'uch', 4, 'besh', 6, 'yetti', 8, 9]
# str_sonlar = []
# int_sonlar = []
#
# for i in sonlar:
#     if type(i) is str:
#         str_sonlar.append(i)
#     else:
#         int_sonlar.append(i)
#
# print(str_sonlar)
# print(int_sonlar)


# --------------------------------------------------------

# tuple - o'zgarmas ro'yxat
# avto_tuple = ('tico', 'damas', 'lacetti', 'spark', 'nexia', 'cobalt')
# avto_list = ['tico', 'damas', 'lacetti', 'spark', 'nexia', 'cobalt']
#
# # print(avto_tuple.__sizeof__())
# # print(avto_list.__sizeof__())
#
# test_list = list(avto_tuple)
# print(type(test_list))
#
# test_tuple = tuple(avto_list)
# print(type(test_tuple))


# --------------------------------------------------------
# range(start, stop, step)

# sonlar = list(range(0, 101, 2))
# print(sonlar)
#
# sonlar = list(range(10, 0, -1))
# print(sonlar)

# daraja = []
# for i in range(1, 11):
#     sq = i ** 2
#     daraja.append(sq)
# print(daraja)

# --------------------------------------------------------
# daraja = [i**2 for i in range(1, 11)]
# print(daraja)


# sonlar = [1, 'ikki', 'uch', 4, 'besh', 6, 'yetti', 8, 9]
#
# list2 = [i for i in sonlar if type(i) is str]
# print(list2)

# --------------------------------------------------------
# juft_sonlar = []
# toq_sonlar = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         juft_sonlar.append(i)
#     else:
#         toq_sonlar.append(i)
# print(juft_sonlar)
# print(toq_sonlar)

# --------------------------------------------------------
# max, min, sum

# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# max_number = max(sonlar)
# min_number = min(sonlar)
# sum_numbers = sum(sonlar)
#
# print(max_number)
# print(min_number)
# print(sum_numbers)

# --------------------------------------------------------
# list[start, stop, step]

# fruits = ['olma', 'anor', 'behi', 'anjir', 'shaftoli', 'apelsin', 'kiwi', 'banan']
# copy_fruits1 = fruits[:]
# copy_fruits2 = fruits[::]
# print(copy_fruits2)
# print(fruits[::2])
# print(fruits[1::2])
# print(fruits[::-1])
# print(fruits[5:])
# print(fruits[:5])
# print(fruits[-2:1:-1])


# --------------------------------------------------------
# fruits = ['olma', 'anor', 'behi', 'anjir', 'shaftoli', 'apelsin', 'kiwi', 'banan']

# no_copy = fruits
# print(fruits)
# no_copy.append('uzum')
# print(fruits)

# 1-usul
# copy_frutis1 = fruits[:]
# copy_frutis1.append('uzum')
# print(fruits)
# print(copy_frutis1)

# 2-usul
# copy_fruits2 = fruits.copy()
# copy_fruits2.append('uzum')
# print(fruits)
# print(copy_fruits2)

# 3-usul
# copy_fruits3 = []
# for el in fruits:
#     copy_fruits3.append(el)
#
# copy_fruits3.append('xurmo')
# print(copy_fruits3)
# print(fruits)