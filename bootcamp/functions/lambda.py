#LAMBDA EXPRESSIONS

#lambda expressions are another way of creating functions
#they are called anonymous functions because they don't have a name (they are a single line of logical code).

# the terms lambda expressions, lambda functions, anonymous functions or function literals can be used interchangeably.

# the general syntax to create a lambda function is   lambda paramater_list: expression

def add(a, b, c):
    result = a + b + c
    return result

#same as above can be done with lambda
r = (lambda a, b, c: a + b + c) (3, 4, 5)
# print(r(1,2,3)) #another method similar to fxn calling
# a lambda expression returns atleast one value it cannot return None
print(r)

square = lambda x: x**2
print(square(4))
# all rules of functions are applicable to lambdas too
square = lambda x=10: x**2 #keyword arguments
print(square())

# a classic example
friends = [('Diana',30), ('Ana', 25), ('Tudor', 22)]
friends.sort(key=lambda x : x[1]) # this sorts by the 2nd element of the tuple
print(friends)

#we can also sort by the lenght of the name
friends = [('Dianaaaaa',30), ('Ana', 25), ('Tudor', 22)]
friends.sort(key=lambda x : len(x[0])) # this sorts by the 2nd element of the tuple
print(friends)