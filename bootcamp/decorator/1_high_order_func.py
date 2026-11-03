#HIGH ORDER FUNCTION
#high order function is a function that either return another function or takes in function as argument

def sum(number, fn): # this fxn is taking in two parameters a function and a number
    result = 0
    for n in range(1, number+1):
        result += fn(n)
    return result

def square(x): # this function will be used as parameter in the first function
    return x ** 2


result = sum(3, square) #the function is being called without a paranthesis

print(result)

#another example
import math
result = sum(10, math.sqrt)
print(result)

# another example in which a function is returned 
def compute(msg):
    if msg == "square":
        return square # nb: square is a function defined above
    else:
        return math.sqrt 

func = compute("square")
print(func(3))

