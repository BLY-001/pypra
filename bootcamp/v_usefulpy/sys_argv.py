#SCRIPTS ARGUMENTS sys.argv

#everytime you execute a command there is a general format first comes the command name and a list of arguments
# separated by space for instance take pip(the python package manager) when we run -- pip install ansible -- 
# pip is the command, install is the first argument and ansible is the second argument, install and ansible are the argument of the command
# this is applicable for each command, this is where sys.argv comes in
#sys.argv where argv stands for argument value is a list in python which contains the command line argument passed to the script
# in the example above sys.argv[0] is pip, sys.argv[1] is install, sys.argv[2] is ansible
#instead of using imput function to grab data from the console, we can actually look art arguments that are passed in when running the scripts

# below is an example
# we create a script here but we will run it manualy from the command line, this is necessary inorder to pass the arguments to the script

import sys
# print(f"Number of arguments: {len(sys.argv)}")
# print(f"this is the name of the script:{sys.argv[0]}")
# print(f"the script arguments are: {sys.argv}")

#lets see another example
# i will make a script that is run with at least one argument, the script arguments are files and it will display them at the console

# first i check that the number of argument is greater than one

if len(sys.argv) > 1:
    for items in sys.argv[1:]:
        with open(items, "r") as f :
            print(f.read())
else:
    print("wrong number of argument the script must be with at least one argument")
