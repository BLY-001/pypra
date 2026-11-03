#OOP: DEFINING CLASSES AND OBJECTS
#to define a class use the class keyword then the class name and a semi colon
class Robot: #the convention is to use the pascal name notation 
    """This class implements a Robot""" #this i a documentation line
    Pass

#from classes we construct instances
#an instance is a specific object created from a particular class below is an example
r1 = Robot() #r1 is an object of class Robot
print(r1.__doc__) #this prints out the doc string of a class