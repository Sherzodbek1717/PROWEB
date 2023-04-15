# 1first way
# import test
# print(test.func1(7, 8))

# # 2nd way
# from test import func1
#
# print(func1(4, 5))
#
# dict1 = dict()
# value = {}
# print(type(dict1))
# print(type(value))

# dict1 = {}
#
# dict1['kampyuter'] = 'mac'
# # dict1['kampyuter'] = ''
#
# print(dict1)
# del dict1['kampyuter']
# print(dict1)

# ---------------------------------------------------------------------------------------
# map(), filter(), lambda funksiyasi

# nums = ['1', '2', '3']
# int_nums = []
# for i in nums:
#     int_nums.append(int(i))
# print(int_nums)

# ---------------------------------------------------------------------------------------
# map(<Nima ish qilish kerakligi>, <qaysi object ustida ish bajarish kerakligi>)

# nums = ['1', '2', '3']
#
# int_list = map(int, nums)
# print(list(int_list))
#
# sonlar1 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# sonlar2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def daraja(son, son2):
#     return son ** son2
#
# map_list = map(daraja, sonlar1, sonlar2)
# print(tuple(map_list))

# ---------------------------------------------------------------------------------------
# filter(<Nima ish qilish kerakligi>, <qaysi object ustida ish bajarish kerakligi>)
# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# def even(num):
#     return num % 2 == 0
# filter_nums = filter(even, sonlar)
# print(list(filter_nums))
# map_nums = map(even, sonlar)
# print(list(map_nums))

# def daraja(son1):
#     return son1 % 2
#
# test = filter(daraja, sonlar)
# print(list(test))

# names = ['abror', 'toxir', 'sobir', 'jalil']
#
# # capitalized_names = map(str.capitalize, names)
# # print(list(capitalized_names))
#
# def do_title(name):
#     return name.title()
#
#
# map_names = map(do_title, names)
# print(list(map_names))

# myList = [
#     1, 'Python',
#     2, 'C',
#     3, 'C++',
#     4, 'Java',
#     5, 'JavaScript',
#     6, 'C#',
#     7, 'Php',
#     8, 'Assembler',
#     9, 'Pascal',
#     10, 'Basic'
# ]
#
# def get_str(el):
#     return type(el) is str
#
# def get_int(el):
#     return type(el) is int
#
# filter1 = filter(get_str, myList)
# filter2 = filter(get_int, myList)
#
# print(list(filter1))
# print(list(filter2))

# ---------------------------------------------------------------------------------------
# lambda(<Nima ish qilish kerakligi>, <qaysi object ustida ish bajarish kerakligi>)
#
# myList = [
#     1, 'Python',
#     2, 'C',
#     3, 'C++',
#     4, 'Java',
#     5, 'JavaScript',
#     6, 'C#',
#     7, 'Php',
#     8, 'Assembler',
#     9, 'Pascal',
#     10, 'Basic'
# ]
#
# filter1 = filter(lambda el: type(el) is str, myList)
# filter2 = filter(lambda el: type(el) is int, myList)
#
# print(list(filter1))
# print(list(filter2))

# a = lambda x: x ** 2
# print(a(10))

#-----------------------------------------------------------------------------
# time

# import time
# # while True:
#
# print(time.strftime('%d/%m/%Y %H:%M:%S'))

# import datetime
# #datetime.datetime to see datetime.py
#
# # print(datetime.datetime.now())
# # print(datetime.datetime.now().year)
# # print(datetime.datetime.now().month)
# # print(datetime.datetime.now().day)
# # print(datetime.datetime.now().hour)
# # print(datetime.datetime.now().minute)
# # print(datetime.datetime.now().second)
# # print(datetime.datetime.now().microsecond)
#
# now = datetime.datetime.now().strftime('%Y/%m/%d')
# print(now)









