#SET METHODS
set1 = {1, 2, 3}
set2 = {2, 3, 1}
print(set1 == set2) #this compares the element
print(set1 is set2) # this compares the addresses

#set1 == set 2 because sets are unordered
#however for ordered sequence like lists it will be false
print([1, 2, 3] == [2, 3, 1])

#1. set.add()
s1 = {1, 2, 3}
s1.add('a')
s1.add(4.5)
print(s1)
s1.add(1) # it does nothing because 1 is alrady an element of the set
# print(s1)

#2. set.remove(item) if the item doesnt exist a "keyerror" is being raised
s1.remove(3) # this removes 3 from the set
print(s1)
#s1.remove(3) #KeyError: 3

#3. set.discard(item) this does nothing even if the item is not in the list
s1.discard('a')
print(s1)
s1.discard('x')

#4. set.pop() this removes and return a random element from the set
x = s1.pop()
print(x, s1)

s2 = set('abc')
s3 = s2 # by using the assignment operator on mutable object like list, sets etc means you are making reference to the same 
# memory address, so changing s3 will change s2 also in the same way
s3.add('x')
print(s2) # "x" is added to s2 because they reference the same memory address

#5. set.clear()
s3.clear() #both s2 and s3 are cleared
print(f's2: {s2}, s3: {s3}')

#6. set.copy() this copies the content of a  set
s4 = s1.copy() #s1 and s4 are diferent sets
s4.add('z')
print(f's4: {s4}, s1: {s1}')
