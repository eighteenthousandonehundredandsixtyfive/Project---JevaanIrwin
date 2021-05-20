import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    value1 = data["list"][0]

print(value1)