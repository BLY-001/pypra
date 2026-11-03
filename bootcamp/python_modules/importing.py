#IMPORTING MODULES
import sys
print(sys.path) #python will search for modules in this directories if it does not find the module in one of this directories the import will fail
#so if you ever run into a problem where python is not able to import a module you should check the sys.path first to make sure the module exist in the path directories
# 1. import name_of_module #this will import all definition such as variable, function or classes from the specified module
import math
#to access a variable or call a function we just write math.name_of_function or variable
print(math.pi)

# 2. we can also import multiple variable by using comma(",")  between them
import random, math, sys
print(random.randint(1, 100))
print(sys.version)

#3. we can also use an alias for the module name
import threading as th #th is an alias for the threading module
print(th.TIMEOUT_MAX)


#4. to directly import all definitions from a module in this case we access the name directly in the module without typing in module_name.variable or function name
from math import * # "*" means all
print(pi)
print(sin(pi))
# this method 4 is not recommended because name collision could occur i.e we have a variable also named pi = 3.14
pi = 3.14
from math import *
print(pi) #the imported pi will overwrite the old one
# inorder to avoid name collision we can use an alias
import math as m
print(m.pi)
#5. importing only some definition from the module, only those defnitions will be available
from math import pi, factorial, sin
print(factorial(10))
# we can also use alias for the definitions too
from math import pi as p, factorial as f, sin as s
print(f(10))
print(s(p))