# __init__ also called the class consructor, its a special method 
#anytime we create a new instance of a class python will automatically look for the __init__ method
#and call it we do not have to call it explicitly
#nb:it is not mandatory for a class to implement the __init__ method its optional
# a method is a function defined inside a class, it will always be called in conjuction with an object using the syntax object_name.method 
class Robot:
    """This class impliments a Robot."""
    def __init__(self, name, year): # the 'self' basically connects methods to the instance of the class, the object that calls the method
        #self can be infact any parameter of our choice it is just conventional to use self, self is not a python keyword
        self.name = name
        self.year = year

r1 = Robot("R1", 2020)  
print(r1.__dict__)
print(f'Robots name:{r1.name}')