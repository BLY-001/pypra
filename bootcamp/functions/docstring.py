#DOCSTRINGS
#commenting and documenting are 2 distinct processes
#docummenting is describing our codes to developers while documenting is describing its use and functiinality to its users
# documenting also creattes a built-in help for dunctions we create 
#docstring is the pop-up window that speaks about what the functions do

def say_hello(name):
    """ this function says hello to you! """
    print(f'Hello {name}! :)')

say_hello('Andrei')
help(say_hello) # you can get the docstring by using help()
#you can also get it by using the dunda doc
print(say_hello.__doc__) #donda doc
# we have two kinds of docstrings one line and multiline doc strings
# multiline docstrings consist of a summary line followed by a blank line and a more elaborate description
# docstrings are not mandatory but highly recommended 
