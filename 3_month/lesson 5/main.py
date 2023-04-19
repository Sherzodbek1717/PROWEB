import psycopg2 as sql


db = sql.connect(
    database='northwind_short',
    host='localhost',
    user='postgres',
    password='123456'
)


cursor = db.cursor()

cursor.execute('''
    select * from customers;
''')

#fetchone() tepadagi qatorni faqat bittasini oladi
# [] called tuple format




# faqat customer nameni ajratib oliw

customers = cursor.fetchall()
for customer in customers:
    customer_name = customer[2]
    print(customer_name)


db.commit()
db.close()


#-------------------------------------------------------------

#
# import psycopg2 as sql
# import requests
#
# db = sql.connect(
#     database='json_17_00',
#     host='localhost',
#     user='postgres',
#     password='123456'
# )
#
#
# cursor = db.cursor()
#
# cursor.execute('''
# drop table if exists posts;
# drop table if exists users;
#
# create table if not exists users(
#     user_id integer generated always as identity primary key,
#     name varchar(50),
#     username varchar(50),
#     email varchar(50)
# );
#
# create table if not exists posts(
#     post_id integer generated always as identity primary key,
#     title text,
#     body text,
#     user_id integer references users(user_id)
# );
# ''')
#
# response = requests.get('https://jsonplaceholder.typicode.com/users')
# users = response.json()
#
#
# for user in users:
#     name = user['name']
#     username = user['username']
#     email = user['email']
#
#     #sqliteda havsiz boliwi ucun ? berilasddi. PostGreSQL da % beriladi
#     cursor.execute('''
#     insert into users (name, username, email)
#     values (%s, %s, %s)
#
#
#     ''', (name, username, email))
#
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# posts = response.json()
#
# for post in posts:
#     title = post['title']
#     body = post['body']
#     user_id = post['userId']
#     print(title, body, user_id)
#
#     cursor.execute('''
#     insert into posts(title, body, user_id)
#     values (%s, %s, %s)
#     ''', (title, body, user_id))
#
#
#
#
#
# db.commit()
# db.close()