# remember a module is a file without the .py extension
import my_math
print(f'a in my_math is {my_math.a}')
s = my_math.my_sum(1,2,3) # we are  calling the function my_sum thats inside my_math.py
print(f'sum is {s}')
#when you import a module into your program python will automatically execute that code inside that module and it will happen only once nomatter how many time we import the module
#NB: importing a module means all codes that are at indentation zero is executed
# i.e if i just write import my_math it will execute all codes at indentation 0
#other programming language have a function called main that is called somewhere at the top of the script and gets aautomtically run
#however in python we do not have such a function but all codes at indentation 0 gets run
print(f'__name__ in my_python_script.py is {__name__}')
