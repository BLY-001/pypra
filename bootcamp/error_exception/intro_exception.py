#INTRO TO EXCEPTIONS
#types of python and exception handling : 1. syntax(parsing)errors, 2. exception(runtime errors)
# syntax errors are identified at compile time before running the script and they are the most common and easiest to find and debug
# a syntax error occurs when the developer doesnt follow python syntax i.e they forget to write a colon when a new block starts or they forget the indentation
#syntax error are mostly underlined in red in most IDE

# for x in range(10) #no semicolon, syntax error
# print(x)

#even though an application can compile without errors during its execution it can generate some, this are called exceptions and are the hardest to find and debug
# exceptions are also called runtime errors you cant know if they have occured until you run the code 
an example of an exception is when you try to write to a file you opened in read mode or when you try to divide a number by zero

# with open('aa.txt') as f:
#     print(f.read()) # this will result in an exception because the file aa.txt does not exist

a, b = 10, 0
#print(a/b) # this will return an exception 'zerodivisionerror'
# print(a + '7') # this will return an exception 'TypeError'

