import os
import json

file = "2-json-to-csv-converter\\json-learning\\01_names.json"

w_dir = os.path.abspath('.')

if os.path.isfile(os.path.join(w_dir, file)):
    with open (file, "r") as json_file:
        data = json.load(json_file)
        name_data = (data["names"])
        for i in name_data: 
            name = (i["firstname"])
            age = (i["age"])
            print (f"{name} is {age}")
else:
    print("No such file exists here '{}'.... ".format(w_dir))