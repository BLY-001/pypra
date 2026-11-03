#OPERATING SYSTEM INTERFACES

# The os module provide function for interacting with the operating system using this functions, we get information on local directories, files, processes and environment variables, 
# lets see some important functions defined inside this module

import os
print(os.getcwd()) # this returns the curent working directory

os.chdir('/home/binlawal') # we use this to change the current working directory to a specified path the argument will be the new directory
# print(os.getcwd())

print(os.listdir())# this returns a list containing the names of entries in the directory given as argument which is the path or if no argument is passed, it will return the entries in the  current working directory
print(os.path.getmtime("/home/binlawal/pypra/bootcamp/v_usefulpy/a.txt"))#this is to get the modification time for the file with its path inside the paranthesis, it prints out the timestamp which is the number of time that has passed since january 1970 

#we want to sort a  directory and findout which file has the biggest timestamp
os.chdir("/home/binlawal/pypra/bootcamp/tuples")
# print(os.getcwd())
print(max(os.listdir(), key=os.path.getmtime))

os.mkdir("/home/binlawal/dir1")# this function is used to create a directory called dir1
#nb but it cannot be used to create folders inside folders inside folders i.e os.mkdir("/home/binlawal/dir1/dir2/dir3")

# but to create folders inside folders like a nested folder we use os.makedirs()
os.makedirs("/home/binlawal/dir2/dir3")