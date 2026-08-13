#SCOPES AND NAMESPACES IN PYTHON

#a namespace is a container(table) that contains the names we define. this way we can have the same name defined in different namespaces
# variables functions and classes are reffered to as namespaces

# the portion of code where the name exists is called the scope of that name and the binding between the name and the value is stored in a namespace
# each scope has its own namespace so both go hand inhand

#in python there are 3 namespaces and scopes:
# 1. the built-in namespace: python built-in functions
# 2. the global (module namespace): names defined in scripts
# 3. the local namespace: names defined inside functions

x = 10 #global variable i.e not inside a func
def my_func():
    print(f'x inside the function:{x}')

my_func() # this will print out 10 because that is the nearest value of x it can access
# in this regard we will say that x has a global scope
#if x is not defined locally inside the function and globally outside it, an error message will be raised

# a local variable is not created until the function is called

x = 10 
def my_func1():
    # x = 5
    global x # in this case the global variable x is now inside the function
    x += 1
    print(f'x inside the function: {x}') 

my_func1()
print(f'x outside the function: {x}')

def len(x): #reasons why keywords should not be used in fxn
    print(x)
# del len #this is used to delete functions
len('abcde') #this will print 'abcde' and not the length
