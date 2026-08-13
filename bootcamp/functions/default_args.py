#FUNCTION DEFAULT ARGUMENTS
# this means giving default valuefor the corressponding parameter when defining a function

def add(x, y = 10, z = 20): #the rule is that if the second argument is made default then all others after it shuld be too
    print(f'x is {x} and y is {x} and z is {z}')
    print(f'y is {x} + {y} + {z} = {x + y + z}')

#calling the functions
add(2, 3) #this reassigns 3 to y and uses the default value for z
add(4)# uses the default value for both y and z
add(6, 7, 8)#assign new values for both y nd z
add(x =9, z=7) # uses the keyword argument to make y default while reassigning value of z