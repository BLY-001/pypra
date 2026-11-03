#INTRO TO OOP:Object Oriented Programming
# OOP is a programing paradigm and is based on classes, objects, attributes and methods
#OOP is an approach for modeling concret real-world objects.
#OOP allows programmers to create their own real-world data types
# a class is a kind of data type, just like a string, integer or list.
# a class is a factory for creating objects.
x = 5
s = 'abc'
l1 = [1, 2]
type(x) #<class 'int'>
type(s) #<class 'str'>
type(l1) #<class 'list'>
#the most important component that make up an object is what it has and what it does,
#in this perspective any object has attributes does different actions implemented as methods
# the data values we store inside an object are called attributes this are what the object has 
# i.e i'm accessing the attribute dunder doc(__doc__) of a list object
l1.__doc__
# __doc__ is an attribute of the object and it describes the object
#on the other hand the function that are associated with the objects are called methods and they
#represent what the object does
l1.append(100) # here append() is a method of the object

#for example: 
# person class:
#   Object(instance):
      #attributes:
        #-name, age, address, salary
      #Methods:
        #- walking, talking, breathing, running
      
#OOP doesn't allow us to do anything we couldn't do without OOP
#its just another way of designing and organizing things
#OOP allows us to structure our code in a human way of thinking
