#CLASS DESTRUCTOR (FINALIZER)
#the destructor is a special function (__del__()) that is automatically called when the lifetime of an object ends
#the purpose of the destructor is to free the resources that the object may have acquired during its lifetime
# in python, destructors aka finalizers are less used , because python has a garbage collector that handles memory management.

class Robot:
    """ this class implements a Robot"""
    def __init__(self, year, name):
        self.name = name
        self.year = year
    #this block is used to delete the entire class
    def __del__(self):
       print('Robot destroyed!')

r1 = Robot(2023, "R1")
print(r1.name) 
print(f'Robot name:{r1.name}')
print(r1.__dict__)