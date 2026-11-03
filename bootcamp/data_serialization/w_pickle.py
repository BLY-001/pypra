#PICKLE DATA SERIALIZATION AND DESERIALIZATION
import pickle
#the native data serialization module for python is pickle its is used to convert python modules to files and 
# then load it when decoding, besides interoperability issues another problem of using pickle is that it is not considered secure
# you should unpickle only data you trust
#nb: using this method you can only serialize or deserialize to python
friends = {"Dan": [20, "London", 3234342], "Maria":[25, "Madrid", 43525222]}
with open("friends.dat", "wb") as f: #"wb" gives the permission to write in binary
    pickle.dump(friends, f)

with open("friends.dat", "rb") as f: #"rb" will give permission to read from a binary file
    obj = pickle.load(f)
    print(type(obj))
    print(obj)

#there is a faster  alternative called cpickle but it doesnt belong to python standard library, you should install it if you want to use it