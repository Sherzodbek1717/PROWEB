# import sqlite3 as sql
#
# db = sql. connect('lesson_3.db')
# cursor = db.cursor()
#
# cursor.executescript('''
#     drop table if exists users;
#     drop table if exists courses;
#
#     create table if not exists courses(
#         course_id integer primary key autoincrement,
#         course_name text
#     );
#
#     create table if not exists users(
#         user_id integer primary key autoincrement,
#         full_name text,
#         course_id integer references coursers(course_id)
#     );
#
#     insert into courses(course_name)
#     values('Python');
#
#     insert into users(full_name, course_id)
#     values ('Toxir Toxirov', 1);
#
# ''')
#
# user = 'Sobir Sobirov'
#
# cursor.execute(f'''
# insert into users(full_name, course_id)
# values (?, 1)
# ''', (user,))
#
#
# cursor.execute('''
# select * from users;
# ''')
#
# users = cursor.fetchall()
# for user in users:
#     print(user[1])
#
# cursor.execute('''
# select count(user_id) from users;
# ''')
#
# count_users = cursor.fetchone()
# print(count_users[0], 'ta foydalanuvchi bor')
#
# db.commit()
# db.close()

#------------------------------------------------------
import datetime
import sqlite3 as sql
import requests
from pprint import pprint

db = sql.connect('weather.db')
cursor = db.cursor()

cursor.executescript('''
drop table if exists cities;
create table if not exists cities(
    city_id integer primary key autoincrement, 
    name text, 
    weather float,
    date text
);
''')

# city_name = 'Tashkent'
# api_key = '996eacfc4d2746453ee42dbe41943ab8'

parameters = {
    'appid': '996eacfc4d2746453ee42dbe41943ab8',
    'units': 'metric'
}

while True:
    city_name = input("Shahar nomini kiriting: ")

    if city_name == 'stop':
        print("Dastur toxtadi!!!")
        break

    parameters['q'] = city_name
    try:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=parameters)
        data = response.json()

        name = data['name']
        temp = data['main']['temp']
        date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        cursor.execute('''
        insert into cities(name, weather, date)
        values (?, ?, ?)
        ''', (name, temp, date))

        print(f'''
{name.title()} shahrida temperatura {temp} gradus.
vaqt: {date}
''')
    except:
        print("shahar nomi notogri kiritildi!")

    # print(name, temp, date)

db.commit()
db.close()
















