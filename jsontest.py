#code for testing json. 
import json
data = {
    "list": [
        1,
        2,
        3,
        4 
    ]
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

