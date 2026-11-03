#INNER FUNCTIONS, CLOSURES AND FREE VARIABLE

def outer():
    msg = "python"
    x = 1
    def inner():
        #if want to modify a non-local or free variable inside the closure you declare that variable with nonlocal bfore changing it
        nonlocal x
        x +=1 
        print(x)#nb: x will continue increasing by one anytime you call the function,-
        # -which simply means the last value of x will always be stored
        print(f"{msg} is really cool") # msg is a free variable (non-local)
    return inner
# in this case the inner function can be regarded as a closure
fn = outer()
fn() # this prints out "python is cool"
# we are calling fn() as a function because the function is returning a function
# a closure is an inner function plus an extended scope that contains the non-local or free varibles

#we can get the list of all free variables of the closure
print(fn.__code__.co_freevars) #this will print out the free variable

# Nb: a closure saves the values of free variables between calls
