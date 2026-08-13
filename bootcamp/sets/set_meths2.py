#SETS METHODS PART2
# ALL SETS METHODS HERE RETURNS A NEW SET
set1 = {1, 3, 5}
set2 = {5, 7, 9}

#1. set.intersection() this method returns the common element in the sets involved
set3 = set1.intersection(set2) # returns the common element in set1 and set2
print(set3)#{5} 
# you can also use ampersand symbol to denote intersection
set3 = set1 & set2 #however the only difference here is that using ampersand(&) as intersetion both arguments must be a set
# however using intersection(item) item can be any iterable, this is applicable to all methods in this session and thier shorthands
print(set3)

#2. set.difference() #creates a set that contains what is present in the first set and not in the second set
set4 = set1.difference(set2) # this contain elements that only belong to set1
print(set4)
#we can also use the minus(-) operator
set4 = set1 - set2
print(set4)

set4 = set1.difference([1, 2, 3, 4, 5]) # this will run based on the explanation in line 10 and 11
# set4 = set1 - [1, 2, 3, 4, 5] #TypeError

#3. set.symmetric_difference() #this means element contained in the sets but they do not have in common
set5 = set1.symmetric_difference(set2)
print(f'set5: {set5}')
#we can also use the chord(^) operator
set5 = set1 ^ set2
print(f'set5: {set5}')

#4. set.union() this is the set of all unique element present in the sets involved
set6 = set1.union(set2)
print(f'set6: {set6}')
#we can also use the pipe(|) operator
print(f'set6: {set6}')

# 5. set.isdisjoint() # two sets are said to be disjoint if they have no element in common
s1 = {1, 3, 5}
s2 = {5, 6, 7}
print(s1.isdisjoint(s2)) #false
s3 = {8, 9}
print(s1.isdisjoint(s3)) #true

# we also have (<, <=, >, >= ) used for containment testing
# < returns true if the set on left hands side is contoained in the sets on the right hands side
print({1, 3} < {1, 2, 3, 4}) #True
print({1,3} <= {1,3}) #True
print({1, 2, 3} > {1, 3}) #True
print({1,2,3} > {0, 1}) #False