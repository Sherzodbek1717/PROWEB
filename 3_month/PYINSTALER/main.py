products = []
while True:
    user_text = input("Komanda va mahsulot nomini kiriting.\n"
                      "Mavjud comandalar stop, add, delete: ")

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
            if product in products:
                products.remove(product)
                print(f"{product} o'chirildi! {products}")
            else:
                print(f"{product} ro'yxatda mavjud emas! {products}")

    else:
        print("Nimadir xato ketdi!")