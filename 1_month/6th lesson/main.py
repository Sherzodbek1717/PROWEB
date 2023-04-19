# -------------------------------------------------------------
# Lug'atlar

# dict1 = dict()
# dict2 = {}
# print(dict1)
# print(dict2)

# avto = {'model': 'Lacetti', 'rang': 'oq'}
# print(avto)

# -------------------------------------------------------------
# Qiymatni kalit orqali olish
# avto = {'model': 'Lacetti', 'rang': 'oq'}
# print(avto['model'])
# print(avto['rang'])

# -------------------------------------------------------------
# Mavjud kalit orqali qiymatni o'zgartish
# avto = {'model': 'Lacetti', 'rang': 'oq'}
# avto['rang'] = 'qora'
# print(avto)

# -------------------------------------------------------------
# Kalit qiymat juftligini qo'shish
# avto = {'model': 'Lacetti', 'rang': 'oq'}
# avto['yil'] = 2022

# -------------------------------------------------------------
# Kalit qiymat juftligini o'chirish
# avto = {'model': 'Lacetti', 'rang': 'oq', 'yil': 2022}
# del avto['yil']
# print(avto)

# -------------------------------------------------------------
# items() metodi yodamida lug'at tarkibini ko'rib chiqish
# avto = {'model': 'Lacetti', 'rang': 'oq', 'yil': 2022}
#
# for key, value in avto.items():
#     print(key, value)


# -------------------------------------------------------------
# Faqat kalit so'zlarni olish. .keys()-metodi
# avto = {'model': 'Lacetti', 'rang': 'oq', 'yil': 2022}
#
# for key in avto.keys():
#     print(key)

# -------------------------------------------------------------
# Faqat qiymatlarni olish. .values()-metodi
# avto = {'model': 'Lacetti', 'rang': 'oq', 'yil': 2022}
#
# for value in avto.values():
#     print(value)

# -------------------------------------------------------------
# Kalitlar yordamida qiymatlarni olish.
# avto = {'model': 'Lacetti', 'rang': 'oq', 'yil': 2022}
#
# for key in avto.keys():
#     print(avto[key])


# -------------------------------------------------------------
# Lug'atdan nusxa olish
# avto = {'model': 'Lacetti', 'rang': 'oq', 'yil': 2022}
# avto2 = {}
# for key, value in avto.items():
#     avto2[key] = value
# print(avto2)

# Lug'atdan nusxa olish .copy() metodi yordamida
# avto = {'model': 'Lacetti', 'rang': 'oq', 'yil': 2022}
# avto2 = avto.copy()
# print(avto2)

# -------------------------------------------------------------
# Lug'atni tozalash clear()

# taomlar = {
#     'osh': 35000,
#     'kabob': 12000,
#     'chuchvara': 22000,
#     "lag'mon": 20000,
#     'somsa': 8000,
# }
#
# print(taomlar)
# taomlar.clear()
# print(taomlar)


# -------------------------------------------------------------

users = [
    {
        'id': 1,
        'name': 'Abror',
        'age': 18,
        'interests': ['reading', 'writing'],
        'info': {
            'work': 'Akfa',
            'city': 'Toshkent'
        }
    },
    {
        'id': 2,
        'name': 'Sobir',
        'age': 45,
        'interests': ['reading', 'writing'],
        'info': {
            'work': 'Akfa',
            'city': 'Toshkent'
        }
    },
    {
        'id': 3,
        'name': 'Zokir',
        'age': 20,
        'interests': ['coding', 'writing'],
        'info': {
            'work': 'Akfa',
            'city': 'Toshkent'
        }
    },
    {
        'id': 4,
        'name': 'Bakir',
        'age': 38,
        'interests': ['reading', 'coding'],
        'info': {
            'work': 'Akfa',
            'city': 'Toshkent'
        }
    },
]


for user in users:
    for key, value in user.items():
        if type(value) is list:
            print(f"{key}:")
            for item in value:
                print(f"--->{item}")

        elif type(value) is dict:
            print(f"{key}:")
            for k, v in value.items():
                print(f"--->{k}: {v}")

        else:
            print(key, value)

    print('-----------------------------')




