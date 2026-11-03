#SYSTEM-SPECIFIC PARAMETERS AND FUNCTIONS 
#the sys module
#sys module provides access to some variables used or maintained by the interpreter and to functions that interact with the python interpreter
#using the sys module we find information about the environment where we can set different environment parameters

import sys

print(sys.version) #prints info on the version nd compilation date
print(sys.implementation) #prints other useful information about the python environment
print(sys.platform) #this prints only the platform such as windows, linux, mac etc 
if sys.platform == "linux":
    print("specific settings and commands for linux")
elif sys.platform == "mac":
    print("specific settings and commands for macos")
elif sys.platform == "win32":
    print("specific setting and command for windows") 
else:
    print("another platform")

print(sys.path) #this prints a list of directories where it will search for the modules we import
my_list = list(range(1_000_000))
my_tuple = tuple(my_list)
my_set = set(my_list)
print(sys.getsizeof(my_list), sys.getsizeof(my_tuple), sys.getsizeof(my_set))

# there are times when we will prefer too save the output to a file before printing or sharing to others
#to do this we use sys.stdout
#i'm going to redirect the output of some command into a file which will be created if it doesnt exist
#

#firstly we save the default stdout into a variable. this way we can restore the default stdout at the end of the script
stdout = sys.stdout
with open("/home/binlawal/pypra/bootcamp/v_usefulpy/a.txt", "a") as sys.stdout:
    print("output redirection...")
    help("sys")

sys.stdout = stdout
with open("/home/binlawal/pypra/bootcamp/v_usefulpy/a.txt", "r") as f:
    print(f.read())

