# def say_hello(*args, **kwargs):
#     pass
#
# say_hello(4, 5)

#
# d = {}
# d['modellar'] = ['Iphone', 'samsung']
# d['colors'] = ['red', 'blue']
# print(d)
#
# print(list(d.keys()))

#------------------------------------------------------------------------------

#Global va Local ozgaruvchilar

# x = 'GLOBAL'
#
# def f1():
#     x = 'local'
#     print("f1 dagi x=", x)
#
# def f2():
#     global x
#     x += 'hello world'
#     print("f2 dagi x =", x)
#
# print(x)
# f1()
# f2()
# print(x)
#
#
#
# def f3():
#     x = 20
#     def f4():
#          x = 60
#          def f5():
#              print("Bu f5 funksiyasi", x)
#          f5()
#          print("Bu f4 funksiyasi", x)
#     f4()
#     print("bu f3 funksiyasi", x)
#
# f3()

#--------------------------------------------------------
# Fayllardan Import qilish

# import module_1
# import module_2
# import module_3
#
# print(module_1.str1)
# module_1.start()

# bowqacha usuli * wu belgi hammasi deganini anglatadi


#
# from module_1 import str1, start
# print(str1)
# start()

# import module_1
# import module_2
# import module_3
#
# print(module_1.str1)
# print(module_2.str1)
# print(module_3.str1)
#
# module_1.start()
# module_2.start()
#psevdanin laqab degan manani bildiradi uzbcasiga

#
# from module_1 import str1 , start
# # from module_3 import str1, start
# from module_3 import str1 as module_3_str1, start as module_3_start
#
# print(str1)
# start()
#
# print(module_3_str1)
# module_3_start()


#--------------------------------------------------------
# papkalardan Import qilish
#
# import fanlar
#
# print(fanlar)
#
# from fanlar.tarix import tarix_labaratory
# from fanlar.fizika import fizika_labaratory
#
# tarix_labaratory.start()
# fizika_labaratory.start()


#--------------------------------------------------------
# packagelardan Import qilish
#
# from fanlar2.adabiyot.adabiyot import asar
# from fanlar2.matematika import geometriya
#
# print(asar)
# print(geometriya.yuza)
#

# from fanlar2 import adabiyot
# print(adabiyot.asar)

import fanlar2
print(fanlar2.asar)



