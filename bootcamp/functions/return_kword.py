#THE RETURN STATEMENT

#we can use the return statement to send back the result of the function to the caller code instead of printing it out

def add2(a, b):
    s = a + b
    return s #this can also return an expression i.e 
    #return a + b the answer will still be dsame
def func1():
    pass# this is a null operation it does nothing even when called

# a fxn should return the result rather than print it because you do not know in what language the user
# who calls the fxn wants the message or how it would be formatted
# your function will not be general and flexible if it prints out messages
# the return statement exit the function any other instruction after return will be ignored
my_sum = add2(5, 2) 
print(my_sum)
x = func1()
print(x)#this will print "None"

# a function can return more than one value and in that case it returns the value as a tuple

def my_func(x):
    return x, x**2, x**3, x**4 #this will be returned as tuples

print(my_func(3)) #this will printout a tuple that contains all the return values
# we can do tuples unpacking so that the answers will not be in tuples
a, b, c, d = my_func(10) # tuples unpacking
print(a, b, c, d)
x, *y = my_func(4) # this is also another type of unpacking and its use when you do not knw the number of returned value
# x is the first return value and *y is a list of the remaining 
print(x, y)