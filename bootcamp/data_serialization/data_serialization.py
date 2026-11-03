#DATA SERIALIZATION

#Data serialization is the process of converting python objects into
#a format for storage, transfer and distribution on physical devices

# an example is wanting to save a  python dictonary  that represent a record on a database into a file and then later load it back into the initial format

# if you try to save a dictionary into a file using write builtin function, you will get an error
# you cannot save a dictionary into a txt file , only a string

#xample
friends = {"DON": [20, "london", 8029293301], "MARIA": [25, "madrid", "8073620019"]}
with open ("friends.txt", "w") as f:
    f.write(friends) # this will return an exception TypeError: write() argument must be str, not dict

#the solution to this problem is to encode or serialize the python object sometimes its necessary to have an exchange format but inother words we want our datas to be imported also in other programming languages or applications
#like saying we have a networking device that gives us structured information