#MAGIC METHODS
#Magic methods are always surrounded by double underscores(__)
# and they are also called special or dunder methods
#dunder is a short name for double underscores, they are special or magic because you don't have to call them directly
#the invocation is automatically done by python interpreter behind the scenes
# they provide simple ways to make object behave like builtin types
# in the case of addition i.e
# a, b = 4, 5
# x, z = '4', '5'
# print(a + b)
# print(x + z)
# # for all this additions __add__() is working under the hood
# a.__add__(b) # consider +-/* as shorthands
# x.__add__(z)
# #there are magic method for each operation, addition, substraction, multiplication,division etc

#we can define magic methods in our classes too to be able to print add,substract or multiply objects etc

class Robot:
    population = 0 #class attribute
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Robot.population += 1 #this will add one anytime an object of the class is called
        
    def __str__(self):
        my_str = f"my name is {self.name} and my price is {self.price}."
        return my_str
    def __add__(self, other): #this is to ensurre addition operation works whenever its called
        price = self.price + other.price
        return price
    
    def __del__(self):
        print('Robot destroyed')

r1 = Robot('Marvin', 150)
r2 = Robot('Gal', 45)
# printing an object will always give us a memory address
print(r1)# to do this we need to add the __str__ method that is automatically called when we need to print an object
print(r1 + r2) # for this to work we need to add the __add__() method
        