# def read_lines(lines, file):
#     file = open(file, mode='r', encoding='utf-8')
#     # 1-usul
#     print(file.readlines()[lines])
#
#     # 2-usul
#     # print(list(file)[lines - 1])
#     # # for f in file:
#     # #     print(f)
#
#
# read_lines(3, 'article.txt')




# ------------------------------------------------------------------
# Json va json moduli

# ------------------------------------------------------------------
# Serializatsiya
# dump() va dumps() meodlari
# import json
#
# data = {
#     "student": {
#         "id": 1,
#         "name": "Abror",
#         "course": "Python"
#     }
# }
#
# data_str = json.dumps(data)
#
# with open('student_info.json', mode='w', encoding='utf-8') as file:
#     json.dump(data_str, file)

# ------------------------------------------------------------------
# Deserializatsiya
# load() va loads() meodlari

# with open('student_info.json', mode='r', encoding='utf-8') as file:
#     content = json.load(file)
#     content_python_obj = json.loads(content)
#     print(content_python_obj['student']['name'])


# ----------------------------------------------------------------

import json
user_language = input("Tilni tanlang: ru, uz: ")
if user_language == 'uz':
    file = open('uz.json', mode='r', encoding='utf-8')
elif user_language == 'ru':
    file = open('ru.json', mode='r', encoding='utf-8')

content = json.load(file)

print(content['messages']['start'])
user_answer = input(content['questions']['start'])

if user_answer == content['answers']['start']:
    user_answer = input(content['questions']['end'])
    if user_answer == content['answers']['end']:
        print(content['messages']['end'])