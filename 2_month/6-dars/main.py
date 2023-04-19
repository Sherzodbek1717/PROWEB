# ------------------------------------------------
# class

# class User:
#     name = 'Abror'
#     lastname = 'Abrorov'
#     age = 45
#
#
# user1 = User
# user2 = User
# user3 = User
#
# user3.name = 'Toxir'
#
# print(user1.name)
# print(user2.name)


# ------------------------------------------------
# __init__() metodi




# class User:
#     def __init__(self, name, lastname, age, salary, work=None):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#         self.salary = salary
#         self.work = work
#         # self.get_user_info()
#
#     def get_user_info(self):
#         print(f"Foydalanuvchi ismi: {self.name}, yoshi: {self.age}")
#
#     def get_user_work(self):
#         if self.work:
#             message = f"Foydalanuvchi {self.work} bo'lib ishlaydi!"
#         else:
#             message = "Ish joyi anketada ko'rsatilmagan"
#         print(message)
#
#
#     def __str__(self):
#         return f"Foydalanuvchi ismi: {self.name} {self.lastname}"
#
#     def __repr__(self):
#         return f"Foydalanuvchi ismi: {self.name} {self.lastname}, yoshi: {self.age}"
#
#     def __eq__(self, other):
#         return self.salary == other.salary
#
#     def __lt__(self, other):
#         # if self.age < other.age:
#         #     return self.age
#         # else:
#         #     return other.age
#         return self.age < other.age
#
#
# user1 = User('Abror', 'Abrorov', 45, 1000, "Konduktor")
# user2 = User('Toxir', 'Toxirov', 52, 1500)

# __eq__() - ==
# __ne__() - !=
# __lt__() - <
# __le__() - <=
# __gt__() - >
# __ge__() - >=

# print(User.__eq__(user1, user2))
# print(User.__lt__(user1, user2))



# print(user1)
# print(user2)


# print(user1.name)
# print(user2.name)
# user1.get_user_info()
# user2.get_user_info()

# user1.get_user_work()
# user2.get_user_work()




# ------------------------------------------------------------------------

class Employee:
    def __init__(self, name, lastname, salary_per_hour):
        self.name = name
        self.lastname = lastname
        self.salary_per_hour = salary_per_hour
        # self.years_of_work = years_of_work

    def __str__(self):
        return self.name

    def get_salary_per_day(self):
        salary_per_day = self.salary_per_hour * 9
        return salary_per_day

    def get_salary_per_month(self):
        salary_per_month = self.get_salary_per_day() * 26
        return salary_per_month

    def get_salary_per_year(self):
        salary_per_year = self.get_salary_per_month() * 12
        return salary_per_year

    def get_full_salary(self, years_of_work):
        full_salary = self.get_salary_per_year() * years_of_work
        user_info = f"Xodim {self.name} {self.lastname} {years_of_work} yil davomida {full_salary}$" \
                    f" daromad olgan!"
        return user_info





employee1 = Employee('Abror', 'Abrorov', 5)

print(employee1)
# print(employee1.get_salary_per_day())
# print(employee1.get_salary_per_month())
# print(employee1.get_salary_per_year())
print(employee1.get_full_salary(50))













