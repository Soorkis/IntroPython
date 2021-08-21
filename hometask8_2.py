

#############################
# persons = [{"name": "John", "age": 15},{"name": "Marina", "age": 15}, {"name": "Jack", "age": 45}, {"name": "Dubina", "age": 45}]
# min_ages = []
# person = min(persons, key=lambda x: x.get('age'))
# min_age = person.get("age")
# for person in persons:
#     if person.get("age") == min_age:
#         min_ages.append(person)
# for person in min_ages:
#     print(person["name"])
#
# longs_names = []
# long_name = max(persons, key= lambda x: len(x.get("name")))
# for person in persons:
#     if len(long_name.get("name")) == len(person.get("name")):
#         longs_names.append(person.get("name"))
# print(longs_names)
#
# ages = [p.get("age") for p in persons]
# average = sum(ages) / len(ages)
# print(average)
#########################################################

my_dict_1 = {"name": "John", "age": 15}
my_dict_2 = {"name": "Marina", "age": 15, "work": "driver"}

keys1 = set(my_dict_1.keys())
keys2 = set(my_dict_2.keys())

lst_1 = list(keys1.intersection(keys2))
lst_2 = list(keys1.difference(keys2))

dict_3 = {}
for key, value in my_dict_1.items():
    if key in lst_2:
        dict_3[key] = value

dict_all = my_dict_1.copy()
for key, value in my_dict_2.items():
    if key in dict_all:
        dict_all[key] = [dict_all[key], value]
    else:
        dict_all[key] = value
print(dict_all)

