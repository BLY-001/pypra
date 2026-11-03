#INSTANCE ATTRIBUTES AND CLASS ATTRIBUTES
# attributes that are uniquue for each instance are called INSTANCE ATTRIBUTE
#CLASS ATTRIBUTES  are attributes that are defined at the class level owned by the class itself and can be shared by all 
#instances of the class, we define class attributes outside the methods at the top right below the class header
class Robot:
    # to access a class attribute we use the notation class_name.class_attribute name
    population = 0 #in this case we want to keep track how many Robots were created
    def __init__(self, name, year):
        self.name = name
        self.year = year
        Robot.population += 1 #once we have another robot add 1 
    def __del__(self):
        print("Robot destroyed")
    #another way to create instance attribute is using common methods
    def setEnergy(self, Energy):
        self.energy = Energy

r1 = Robot("R1", 2020)
r2 = Robot("Ben", 2040)
print(r1.__dict__)
# we are caling the method on an object
r1.setEnergy(500)
print(r1.energy)
# another way to get the value of an attribute is to use the builtin getattr() method
#getattr(object,'attribute_name')
# you can also use getattr() to give a default value for the attribute as the third value to avoid error 
print(getattr(r1, 'brand', 'N/A')) #this will print out "N/A" as value of brand
print(f'Robots alive: {Robot.population}')


