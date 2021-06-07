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

a = 1
a = str(a)
b = "str"
print (a + ' ' + b)
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

