# Funksiyalar
# ----------------------------------------------------------



# def say_hello(first_name, last_name, age, address='Toshkent', email=None):
#     print(f"Salom! {first_name} {last_name}, {2023 - age}-yilda tavallud topgansiz\n"
#           f"Yashash joyi: {address}")
#     if email:
#         print(f"Email: {email}")
#
# ism = 'Akmal'
# familiya = 'Akmallov'
# yosh = 38
# manzil = 'Qashqadaryo'
#
# say_hello(ism, familiya, yosh, manzil, 'alfa@gmail.com')
# say_hello('Abror', 'Abrorov', 45, 'Sirdaryo')

# say_hello(45, 'Abrororv', 'Abror')
# say_hello('Abror', 'Abrorov', 45)
# say_hello(age=45, first_name='Abror', last_name='Abrorov')



# def say_hello(FIO, manzil, age, phone = None, email = None):
#     info = f"Foydalanuvchi - {FIO}, address -{manzil}, yoshi - {2023 - age}\n"
#     if phone:
#         info += f"Phone: {phone}\n"
#     if email:
#         info += f"email: {email}\n"
#     return info
#
#
# def get_work(info, work):
#     user_info = info
#     user_info += f"{work} kompaniyasida ishlaydi"
#     print(user_info)


# full_info = say_hello(FIO='Karimov Samandar', manzil=' TTZ dahasi', age=19, phone='+998 99 *** ** 01', email='beta@gmail.com')
# get_work(full_info, 'akfa')


# full_info = say_hello(FIO='Karimov Samandar', manzil=' TTZ dahasi', age=19, phone='+998 99 *** ** 01', email='beta@gmail.com')
# print(full_info)


# -----------------------------------------------
# Funksiyadan lug'at qaytarish

# def avto(name, color, year, price, position, take_out=None):
#     info = {
#         'name': name,
#         'color': color,
#         'year': year,
#         'price': price,
#         'position': position,
#     }
#
#     if take_out:
#         info['take_out'] = take_out
#
#     return info
#
# avto1 = avto('Malibu', 'black', 2023, 40000, 'turbo+', '9-oy')
# avto2 = avto('Malibu', 'black', 2023, 40000, 'turbo+')
#
# cars = [avto1, avto2]
#
# print(cars)

# -----------------------------------------------
# Funksiyadan ro'yxat qaytarish

# def intermediate(min, max, step=1):
#     nums = []
#     while min < max:
#         nums.append(min)
#         min += step
#     return nums
#
# print(intermediate(1, 100, 2))


# -----------------------------------------------
# Ixtiyoriy cheklanmagan pozitsion argumentlar


# def summa(*args):
#     return sum(args)
# print(summa(4, 5, 5, 5, 4, 5, 7, 8))


# -----------------------------------------------
# Ixtiyoriy cheklanmagan nomlangan argumentlar

def cars(model, color, **kwargs):
    kwargs['model'] = model
    kwargs['color'] = color
    return kwargs

print(cars('Malibu', 'white', magnitafon=True, chixol=True, kamera=True, lyuk="Tonirovka qilingan"))