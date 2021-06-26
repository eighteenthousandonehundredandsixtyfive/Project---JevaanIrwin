#code for testing json. 
import json
a =321

data = {
    "list": [
        1,
        2,
        3,
        4 
    ], 
    'test':[
        123
    ], 
    'a': a
}

nested_dictionary ={'dic_one': {'age': '12', 'name': 'benjamin', "lastname": 'irwin'},
                    'dic_two': {'age': '17', 'name': 'jevaan', "lastname": 'irwin'}}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent = 2)



