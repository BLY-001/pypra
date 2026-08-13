#LIST CONCATENATION
l1 =[3, 4]
print(l1, id(1))
l1 = l1 + [5, 6]
print(l1, id(l1)) #this will produce a different id from the initial
# l1 because a completely new list has been created
l1 +=[7, 8]
print(l1, id(l1)) 

l1.extend([11, 12]) #the object inside extend must be an iterable
print(l1, id(l1)) #this will also reference the same id address

# append vs extend
# append adds a single item to the end of the list 
# while extend extends the list by adding all the items from an iterable
l1.append(['a', 'b'])
print(l1)
l1.extend(['x', 'y'])
print(l1)
l1.append(20)
l1.extend([20]) # both l1.append(20) and l1.extend([20]) does thessame thing
# we just had to convert 20 to a list which is an iterable before we can use extend
# however l1. extend(20) will not work because 20 (int) is not an iterable

#repetition
# this will produce the content of the list the number of times it has been multiplied
l2 = list('abc')
l3 = l2 * 3 # l2 is treated as ['a', 'b', 'c'] and it will be written 3 times in the same list
print(l3)