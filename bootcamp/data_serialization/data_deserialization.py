#DATA DESERIALIZATION

import json
with open("friends.json", "rt") as f:
    obj = json.load(f) # this is to load the json file

    # nb: just like we have dump(serialises from file)and dumps(serialises from json string), we also have load(deserialises from file) and loads (deserialises from json string)
    print(type(obj))
    print(obj)

json_string =""" {"Dan": 
[20, "London", 3234342], 
"Maria": 
[25, "Madrid", 43535465]}"""
#json does not support single quotes only double quotes for strings

#to load this json string into a python dictionary
obj = json.loads(json_string)
print(type(obj))
print(obj)

#nb: json are not 100 percent compatible with python data types
# list and tuple are treated as array
# set is not json serializable you must convert it to a set first or use pickle instead

