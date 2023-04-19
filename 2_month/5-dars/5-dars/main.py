# import requests
# from pprint import pprint
# import json
#
# req = requests.get('https://jsonplaceholder.typicode.com/posts')
# posts = req.json()
#
# json_data = []
# for post in posts:
#     userId = post['userId']
#     post_id = post['id']
#     post_title = post['title']
#     post_body = post['body']
#
#     if post_id > 20:
#         break
#
#     user_req = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
#
#     user = user_req.json()
#
#     name = user['name']
#     username = user['username']
#     email = user['email']
#     address = f"City: {user['address']['city']}, street: {user['address']['street']}"
#
#     json_data.append({
#         'post': {
#             'id': post_id,
#             'title': post_title,
#             'body': post_body
#         },
#         'user': {
#             'id': userId,
#             'name': name,
#             'username': username,
#             'email': email,
#             'address': address
#         }
#     })
#
# with open('posts_and_users.json', mode='w', encoding='utf-8') as json_file:
#     json.dump(json_data, json_file, indent=4)


# -----------------------------------------------------------------------------
# weather

import requests
from pprint import pprint

parameters = {
    'appid': 'b01e7608c07f15c54ff9d9b64d478705',
    'q': 'Tashkent'
}

data = requests.get(f'https://api.openweathermap.org/data/2.5/weather', params=parameters).json()

pprint(data)











