# PYTHON SETS
# sets are unordered collection of unique elements
s1 = {1, 2, 3, 'a', 'b', 4}
# you cannot get the element of a set using indexing
print(s1)
# print(s1[0]) #ERROR
# sets also do not allow duplicates each element appears once
#sets are mutable, it can be modified
#adding a tuple to the set
s1.add((10,20))
print(s1)
#removing an element from a set
s1.remove('a')
print(s1)
#the elements of a set can be different types but all of them must be immutable 
# a list cannot be an element of a set
ll = [1, 2]
#s1.add(l1) #TYPE ERROR

# to create an empty set we use a set constructor
s2 = set()
# a pair of empty curly braces gives a dictionary
s3 = {}
print(type(s3), type(s2))

# str ==> set
s4 = set('helloooooo!!!')
print(s4)

# tuple ==> set
s5 = set((1, 2, 3, 4, 4, 'abc'))
print(s5)

# list ==> set
l2 = [10, 20, 30, 40]
print(set(l2))

# the common usecase of sets is to remove dduplicates from other data structures
macs = ['30-24-32-e2-0f-59','30-24-32-e2-0f-59','30-24-32-e2-0f-59','30-24-32-e2-0f-80']
mac_addresses = set(macs)
print(mac_addresses)
print(len(mac_addresses))
print(list(mac_addresses))

# set is an iterable you just dont know the order
for item in s4:
    print(item)
