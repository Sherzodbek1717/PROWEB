# Ro'yxatlar

# list1 = []
# list2 = list()

# list1 = ['olma', 'banan', 'olcha', 'anor']
# sonlar = ['bir', 'ikki', 3, 4, 'besh', 6, 'yetti', 8, 9]
#
# print(list1)
# print(sonlar)

# -----------------------------------------------
# Ro'yxatga indexi orqali murojaat qilish

# list1 = ['olma', 'banan', ['kiwi', 'nok', ['uzum', 'anjir', ['aplesin']]], 'olcha', 'anor']
# print(list1[1])
# print(list1[0])
# print(list1[-1])
# print(list1[-2])
# print(list1[2][2][2][0])

# -----------------------------------------------
# Index bo'yicha elementlarni o'zgaritish
# list1 = ['olma', 'banan', ['kiwi', 'nok', ['uzum', 'anjir', ['aplesin']]], 'olcha', 'anor']
#
# list1[0] = 'shaftoli'
# list1[2] = 'uzum'
# print(list1)

# -----------------------------------------------
# len() - funksiyasi
# list1 = ['shaftoli', 'banan', 'uzum', 'olcha', 'anor']
#
# count_list = len(list1)
# print(count_list + 5)

# text = 'test'
# print(len(text))

# -----------------------------------------------
# .append(), .insert() - metodlari

# ismlar = []
#
# ismlar.append('Abror')
# ismlar.append('Aziz')
# ismlar.append('Toxir')
# ismlar.append('Sobir')
# print(ismlar)

# ismlar2 = ['Abror', 'Aziz', 'Toxir', 'Sobir']
# ismlar2.insert(1, 'Abdulla')
# ismlar2.insert(-2, 'Sadir')
# print(ismlar2)

# -----------------------------------------------
# del - operatori, .remove(), .pop() - metodlari

# names = ['Abror', 'Abdulla', 'Aziz', 'Sadir', 'Toxir', 'Sobir']

# del names[2]
# print(names)
#
# names.remove('toxir'.title())
# print(names)
#
# name = names.pop(0)
# print(names)
#
# new_names = []
# new_names.append(name)
# print(new_names)

# -----------------------------------------------
# .sort() - metodi

# names = ['abror', 'Sadir', 'Toxir', 'abdulla', 'Sobir', 'Aziz', 'behruz', 'Jalil', 'Asad', 'Ziyod', 'Jamshid']
# names.sort(reverse=True)
# print(names)

# -----------------------------------------------
# sorted() - funksiyasi

# names = ['abror', 'Sadir', 'Toxir', 'abdulla', 'Sobir', 'Aziz', 'behruz', 'Jalil', 'Asad', 'Ziyod', 'Jamshid']
# copy_names = sorted(names)
#
# print(copy_names)
# print(names)

# -----------------------------------------------
# .index() va .count() metodlari

# numbers = [4, 5, 78, 94, 5, 6, 32, 21, 5, 74, 6]
# count_element = numbers.count(5)
# # print(count_element)
#
# # index(value, start, stop)
# index_element = numbers.index(6, 4, 8)
# print(index_element)


# -----------------------------------------------
# in va not in komandalari

# taomlar = ['osh', 'lagmon', 'manti', 'shorva', 'somsa']
#
# taom = input("Taom nomini kiriting: ").lower()
#
# # result = taom in taomlar
# # result = taom not in taomlar
# # print(result)
#
# if taom in taomlar:
#     print(f"{taom.title()} savatga qo'shildi")
# else:
#     print(f"Kechirasiz {taom.title()} yo'q!")


# -----------------------------------------------
# Satrdan ro'yxat xosil qilish .split() - metodi

# text = 'Hello World'.split()
# print(text)

# names = input('Ismlarni kiritring: ').split(', ')
# print(names)

# -----------------------------------------------
# Ro'yxatdan satr xosil qilish .join() - metodi

names = ['Abror', 'Sobir', 'Toxir']
names_str = ', '.join(names)
print(names_str)




