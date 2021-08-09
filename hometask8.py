# my_list = ["sdjkjf", "qweryter", "eruaug", "teudgs"]
#
#
# def reverse_lst(my_list):
#     my_list2 = []
#     for indexl, vallist in enumerate(my_list):
#         if indexl %2 == 0:
#             my_list2.append(vallist[::-1])
#         else:
#             my_list2.append(vallist)
#     return my_list2
#
# print(reverse_lst(my_list))

########################################


# my_list = ["sdjkjf", "aweryter", "eruaug", "teudgs"]
# def start_a(lst1):
#     lst2 = []
#     for i in lst1:
#         if i.startswith('a'):
#             lst2.append(i)
#     return lst2
# print(start_a(my_list))
##########################################################
# my_list = ["sdjkjf", "aweryter", "eruaug", "teudgs"]
# def start_a(lst1):
#     lst2 = []
#     for i in lst1:
#         if 'a' in i:
#             lst2.append(i)
#     return lst2
# print(start_a(my_list))
####################################################

# my_list = ["sdjkjf", "aweryter", 21, 3554, "eruaug", "teudgs"]
# def start_a(lst1):
#     lst2 = []
#     for i in lst1:
#           if type(i) == str:
#             lst2.append(i)
#     return lst2
# print(start_a(my_list))
####################################################

# my_str = 'sdjkjf, aweryter, 21, 3554, eruaug, teudgs'
# def start_a(lst1):
#     lst2 = []
#     for i in lst1:
#         if lst1.count(i) == 1:
#             lst2.append(i)
#     return lst2
# print(start_a(my_str))
#######################################

# my_str = 'sdjkjf, aweryter, 21, 3554, eruaug, teudgs'
# my_str2 = 'djkjf, aweryter, 21, 3554, eruasdjkf, 126kjsdh, 234.112'
# def start_a(my_str, my_str2):
#     set1 = set(my_str)
#     set2 = set(my_str2)
#     my_str3 = list(set1.intersection(set2))
#     return my_str3
# print(start_a(my_str, my_str2))

# import random
# import string
# from string import ascii_lowercase as letters
#
# names = ["krab", "usach", "barabashka"]
# domains = ["net", "com", "hop"]
# mail_dig = random.randint(100, 1000)
# print(mail_dig)
# mail_symbol = ''.join([random.choice(letters) for _ in range(random.randint(3, 6))])
# print(mail_symbol)
# def create_email():
#     choice_name = random.choice(names)
#     choice_domains = random.choice(domains)
#     mail_symbol = ''.join([random.choice(letters) for _ in range(random.randint(3, 6))])
#     mail_dig = random.randint(100, 1000)
#
#     e_mail = choice_name + str(mail_dig) + "@" + mail_symbol + "." + choice_domains
#     return e_mail
#
# print(create_email())









