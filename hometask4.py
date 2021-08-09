# import random
# my_list = []
# for _ in range(3):
#     number = random.randint(0,256)
#     my_list.append(number)
# print(my_list)
# for number in my_list:
#     if number > 100:
#         print(number, chr(number))
# my_results = []
# for number in my_list:
#     if number > 100:
#         my_results.append(number)
# print(my_results)
# if len(my_results) < 2:
#     my_results.append(0)
# else:
#     s = my_results[-1] + my_results[-2]
#     my_results.append(s)
# print(my_results)


# value = input("Number: ")
# try:
#     value = float(value)
#     print(value ** -1)
# except Exception:
#     print('Incorrect input. Try again.')

# my_results2 = []
# for index, value in enumerate(my_list):
#     s = index + value
#     if s%2 == 0:
#         my_results2.append(value)
# print(my_results2)


# my_string = "0123456789"
# lst = []
# for tenner in my_string:
#     for unit in my_string:
#         # print(tenner,unit)
#         num = tenner + unit
#         # print(num, type(num))
#         num = int(num)
#         # print(num, type(num))
#         lst.append(num)
# print(lst)
