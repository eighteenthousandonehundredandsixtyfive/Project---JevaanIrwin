import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    value1 = data

print(value1)
print(value1["dic_one"]['age'])
del value1["dic_one"]
print (value1)