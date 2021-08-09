# my_list = ["sdjkjf", "qweryter", "eruaug", "teudgs"]
# my_list2 = []
# for indexl, vallist in enumerate(my_list):
#     if indexl %2 == 0:
#         my_list2.append(vallist[::-1])
#     else:
#         my_list2.append(vallist)
# print(my_list2)
###########################################

# my_list = ["sdjkjf", "qweryter", "aruaug", "teudgs", "askjdakj"]
# my_list2 = []
# for word in my_list:
#     letter = word[0]
#     if letter == "a":
#         my_list2.append(word)
# print(my_list2)
###############################################

# my_list = ["sdjkjf", "qwerytaer", "aruaug", "teudgs", "askjdakj"]
# my_list2 = []
# for word in my_list:
#     for letter in word:
#         if letter == "a":
#             my_list2.append(word)
#             break
# print(my_list2)
#
# my_list2 = []
# for word in my_list:
#     if 'a' in word:
#         my_list2.append(word)
# print(my_list2)
########################################################

# my_list = [1, 343, 66745, 2, "12", "634"]
# my_list2 = []
# for my_str in my_list:
#     if type(my_str) == str:
#         my_list2.append(my_str)
# print(my_list2)

##########################################

# import random
#
# from string import ascii_lowercase
#
# my_str = [random.choice(ascii_lowercase) for _ in range(random.randint(10, 21))]
# my_str = ''.join(my_str)
# print(my_str)
# my_str2 = []
# for letter in my_str:
#     if my_str.count(letter) == 1:
#         my_str2.append(letter)
# print(my_str2)

#########################################

# import random
# import time
# from string import ascii_lowercase
#
# my_str = [random.choice(ascii_lowercase) for _ in range(random.randint(10, 21))]
# my_str = ''.join(my_str)
# my_str2 = [random.choice(ascii_lowercase) for _ in range(random.randint(10, 21))]
# my_str2 = ''.join(my_str2)
# my_str3 = []
# start = time.time()
# # print(start)
# for letter in my_str:
#     if letter in my_str2:
#         my_str3.append(letter)
# my_str3 = list(set(my_str3))
# print(time.time() - start)
# print(my_str3)
#
# start = time.time()
# my_str4 = list(set(my_str).intersection(set(my_str2)))
# print(time.time() - start)
# print(my_str4)

##########################################################
#
# import random
# import time
# from string import ascii_lowercase
#
# my_str = [random.choice(ascii_lowercase) for _ in range(random.randint(10, 21))]
# my_str = ''.join(my_str)
# my_str2 = [random.choice(ascii_lowercase) for _ in range(random.randint(10, 21))]
# my_str2 = ''.join(my_str2)
# my_str3 = []
# my_str4 = []
# for letter in my_str:
#     if my_str.count(letter) == 1:
#         my_str3.append(letter)
# for letter in my_str:
#     if my_str.count(letter) == 1:
#         my_str4.append(letter)
# my_str5 = list(set(my_str).intersection(set(my_str2)))
# print(my_str5)

#################################################
# import json
#
# infopeople = {
#     "lastname": "Абрамов",
#     "name": "Юрий",
#     "age": "43",
#     "place": {
#         "country": "Юар",
#         "city": "Йоханес",
#         "street": "Бурунду"
#     },
#     "work": {
#         "yesnot": "есть",
#         "post": "пастор"
#     }
# }
# print(json.dumps(infopeople, indent=4, ensure_ascii=False))
# print(infopeople)

###############################################################

import json

# cake_recipe = {
#     {"const": "Ингридиенты"},
#     {"cakes": "Коржи"},
#     {"flour": "Мука", "200 грамм"
#     "milk": "Молоко", "500 ml"
#     "butter": "Масло", "100 грамм"
#     "eggs": "3 шт"},
#     {"cream": "Крем"},
#     {"sugar": "Сахар", "100 грамм",
#     "oil": "Масло",  "30 ml",
#     "vanilla": "Ваниль", "20 грамм"},
# }

# cake_recipe = {
#     'cakes': {
#         'flour': '100 gramm',
#         'milk': '250 ml',
#         'butter': '100 gramm',
#         'eggs': '3 ps',
#     },
#     'cream': {
#         'sugar': '100 gramm',
#         'oil': '30 ml',
#         'vanilla': '50 gramm',
#         'sour cream': '50 gramm',
#     },
#     'glaze': {
#         'cocoa': '30 gramm',
#         'sugar': '100 gramm',
#         'butter': '50 gramm',
#     }
# }
#
#
# print(json.dumps(cake_recipe, indent=4, ensure_ascii=False))
# print(cake_recipe['cream']['vanilla'])