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


def f3():
    x = 20
    def f4():
         x = 60
         def f5():
             print("Bu f5 funksiyasi", x)
         f5()
         print("Bu f4 funksiyasi", x)
    f4()
    print("bu f3 funksiyasi", x)

f3()



