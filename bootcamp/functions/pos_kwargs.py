#FUNCTION POSITIONAL AND KEYWORD ARGUMENTS

# a function can take parameters that are a special kind of variable used in a function as input
#five types of function arguments in python 1. Positonal arguments 2. Keyword arguments 3. Default arguments 4. *args 5. **kwargs

def difference(a, b):
    result = a - b
    print(result)
# you must pass same number of argument as in the fxn parameters otherwise error
difference(1, 5)

# parameters vs arguments
#parameters are variables local to the fxn
# arguments are passed into the function when calling it
def func1(x, y): #x and y are function parameters
    print(f'1st parameter x is {x}')
    print(f'2nd parameter y is {y}')

func1('python', 55) #python and 55 are arguments passed to the fxn

#keyword arguments also called named arguments basically allow us to ignore the order of the functions argument when we call it
def func1(x, y, z):
    print(f'1st parameter x is {x}')
    print(f'2nd parameter y is {y}')
    print(f'3rd parameter z is {z}')

func1(y=7, x =3, z=9) #keyword args in action
#nb : you can mix both positonal and keyword args together just ensure that positional comes before the keyword args otherwise it will throw an error
# i.e  func1(6, z=1, y=9)
