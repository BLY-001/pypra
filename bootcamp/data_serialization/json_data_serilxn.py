#JSON DATA SERIALIZATION (Javascript Object Notation)
# this is a lightweight data interchange format inspired by javascript object literal syntax(although it is not a strict subset of javascript)

import json

# you go with json if you want interoperability between applications outside the python ecosystem
# or you want a text format to store your data nb: json is more secure than pickle
# unlike pickle deserilization on json does not create an arbitrary code execution vulnerability

# json is preferred over pickle in most cases however their is one major drawback, json by default can only represent a subset of the python builtin class and no custom classes
# pickle can represent an extreme large number of python types

# in a nutshell you use pickle when you are not interested in interoperability and security is not of any concern to you
# and you want to load thesame data that has been serialized back into python objects

# you use json when you need interoperability between applications security concerns and you are not interested in preserving evry python data type

friends = {"Dan": [20, "London", 3234342], "Maria":[25, "Madrid", 43535465]}

#the json module has two functions for serializing python objects into json format : dump which save the data to file on disc and dumps which takes the python object and return the json encoded string

# using dump
with open("friends.json", "w") as f:
    json.dump(friends, f, indent=4) # indent is used to control the indentation size of nested structures

#using dumps
json_string = json.dumps(friends, indent=4)
print(json_string)

#json is meant to be easily readable by humans
#in this example we have a very simple dictionary  imagine what the json string looklike if we serialized tons of informotion it will be squezzed together
#their is an attribute called indent that controls the indentation size of nested structures