# INTRO TO PYTHON MODULES

# a module is a file containong python definitons and statement such as variables,
# functions,classes etc;
# the file name is the module name with suffix .py appended;
# e.g automation.py is the file and automation is the module;
# python modules and packages are two mechanisms that faciltate modular programming;
# before using a module, we must import it!

#python modules and pacakages are two mechanism that facilitates modular programming which is a way of breaking larger task into separate more manageble subtask or modules
#individual moduls can then be comibned like building blocks for larger application
import math #we are importing a module called math
print(type(math))
print(math.sqrt(2))# calling a function from math module
dir(math) #this gives all functions and variables defined in the module

#types of modules
#Built in modules: thry come with python and are part of so called python standard library
#external modules: they are not included in the standard python installation. they must be downloaded from the internet
#pip is a simple utility that downloads and installs modules and packagesat you command line directly from the internet;
# display all available modules:
# help(modules)
# modules have been written either in python itself or in c  