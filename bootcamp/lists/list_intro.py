l1 = [1, 2.5, "python", True, ["abc", "xyz"], (10, 20, 30)]
# A list can contain several data types 
print(len(l1))
l2 = [] #empty list declaration
l3 = list() # empty list declaration by calling the constructor of the list class
print(l1[0]) # printing the first element of l2
x = l1[-1] # using negative number to slice from the right hand side
print(x)
# if you tried to access an element that do not exist you will get an index out of range error 
s1 = 'abc' #strings are immutable cannot be changed
# s1[0] = 'x' # this will give a type error
# list are mutable hence the elements can be changed
l4 = list('abcd')
print(l4)
print(id(l4))
l4[0] = 'x'
l4.append(100)
print(l4)
print(id(l4))
# despite adding and changing the elements in a its still maintain the same id 
