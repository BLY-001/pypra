#SCOPES AND NAMESPACES 2

numbers = [1, 2, 3]
x = 10
def my_function(numbers, x):
    numbers.append(5)
    x = 66 #when python sees an assigmnent inside a function it creates a new local scope variable
    print(f'x inside the function: {x}')

my_function(numbers, x)
print(f'after calling the function, number is {numbers} and x is {x}')
