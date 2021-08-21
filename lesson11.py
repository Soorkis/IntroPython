import  json


def gets_json(path):
    with open(path) as file:
        data = json.load(file)
        return data

data = gets_json('data.json')
print(data)
###################################

def sort_by_name(data):
    lst = []
    for d in data:
        name = d.get("name")
        last_name = name.split()[-1]
        lst.append(last_name)
    return  sorted(lst)

print(sort_by_name(data))
############################

def sort_by_lastname(data):
    return sorted(data, key= lambda d: d.get("name").split()[-1])
print(sort_by_lastname(data))
################################

def sort_by_deth(d):
    years = d.get("years").split("-")[-1]
    digist_lst = list(filter(str.isdigit, years))
    digist_str = ''.join(digist_lst)
    digist = int(digist_str)
    if "BC" in years:
        digist = - digist
    return digist

def sort_file_by_deth(data):
    return sorted(data, key=sort_by_deth)
print(sort_file_by_deth(data))
##################################

def sort_by_text(data):
    return sorted(data, key= lambda d: len(d.get("text").split()))
print(sort_by_text(data))