# import random
#
# number = random.randint(10**20, 10**30)
# number = str(number)
# zero = number.count("0")
# print(number, zero)

# import random
#
# number = random.randint(10, 99)* 10**random.randint(1, 10)
# print(number)
# number = str(number)
# lennum = len(number)
# lennum2 = len(str(int(number[::-1])))
# zero = lennum - lennum2
# print(zero)

###################
# my_list = [1,2,3,4]
# end = my_list.pop()
# new_list = my_list.insert(0, end)
# print(my_list)

#########################

# my_str = 'Bkakbkab 56 bkobko 45 fgfgdgh 65  ggtgt'
# my_lst = my_str.split()
# print(my_lst)
# ssum = 0
# for new_str in my_lst:
#     if new_str.isdigit():
#         new_str = int(new_str)
#         ssum += new_str
# print(ssum)

##########################

# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
#
# r_index = my_str.rfind(r_limit)
# l_index = my_str.find(l_limit)
#
# limitmax = my_str[l_index + 1:r_index]
# print(limitmax)

###########################
# import random
# from string import ascii_lowercase as letters
#
# my_str = ''.join([random.choice(letters) for _ in range(random.randint(2, 15))])
# print(my_str)
# my_list = []
# my_str = my_str + '_' if len(my_str) %2 == 1 else my_str
# for i in range(0,len(my_str),2):
#     my_list.append(my_str[i:i + 2])
# print(my_list)

##########################

# import random
#
# my_list = [random.randint(10, 99) for _ in range(random.randint(8, 35))]
# print(my_list)
# my_count = 0
# for i in range(1, len(my_list) - 1):
#     # left = my_list[i - 1]
#     # right = my_list[i + 1]
#     # centre = my_list[i]
#     # left, centre, right = my_list[i - 1: i + 2] not my, only example
#     if centre > left + right:
#         my_count += 1
# print(my_count)