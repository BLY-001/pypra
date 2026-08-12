
person = {'name': 'john', 'age': 30, 'location': 'USA'}
#dict.key() # this method gets the keys in the dict
k = person.keys()
print(k)
print(type(k)) #<class 'dict_keys'>
#dict keys can be easily converted to lists
my_keys = list(k)
print(my_keys)

# dict.value() this also returns the values of a dictionary
print(person.values())
# this can also be converted to a list
print(list(person.values()))

# dict.items() it returns a view of the dictionary's item or key,value pairs in a tuple
print(person.items()) # the result of this looks like a list of tuples each tuple beign the key,value pair

#checking for membership in a dict

print('name' in person) # True
#to check if 10 is a key in person
print(10 in person.keys())# false
#to check for a value in a dict
print('USA' in person.values())

# you can also check if a specific pair exist in a dict
print(('age', 30) in person.items())
#NB : THE DICT RETURNED BY ANY OF THIS METHODS ARE DYNAMIC AND REFLECT ANY CHANGES IN THE ORIGINAL DICTIONARY

d1 = {10: 'a', 20: 'b', 30: 'c'}
v = d1.values() # v is used to short view
d1[10] = 'X' #this change affects the original value of the dict and the value in V because they are still dynamically connected to the dictionary
print(v)

#dictionary views and item methods behave like sets because their items are unique
d1 = {10: 'a', 20: 'b'}
d2 = {20: 'c', 30: 'c'} 
k1 = d1.keys()
k2 = d2.keys()
print(k1, k2)

#dictionary keys behave like sets, you can use set methods on them but only the short forms
print(k1 & k2) 
print(k1 | k2)

#iterating over a dictionary
#using keys
for k in person:# you can also use "for k in personz.keys(): 
    print(f'key is {k}')

#using values
for v in person.values():
    print(f'value is {v}')

# iterating over keys and values
for k in person.keys():
    print(f'k is {k} and value is {person[k]}')
#second method
for k,v in person.items():
    print(f'the key is {k} and the value is {v}')

