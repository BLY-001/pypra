# LIST METHODS PART 2
#7. list.index() this returns the index of the specified element within a list
names = ['john', 'dan', 'tom', 'john', 'bill']
i = names.index('dan')
print(f'dan is at index {i}') # it raises a value error if the item is not in the list
# arguments  like names.index('dan', 1, 3) can also be used
# which means find dan between index 1 and index 3 excluded
#if there are duplicates it returns only the first occurence

#8. list.count() it returns the number of times an elemnt appears in the list
letters = list('addshgafdytdfythdsjshgewy')
n = letters.count('a')
print(n)
 # membership of an element in list is best checked using in
print('b' in letters)

#9. list.reverse() this just reverse the element in place
l1 = [1, 3, 'abc', 10, 'x']
l1.reverse()
print(f'l1: {l1}')

#10. list.sort() and sorted(list)
#sorted(list) returns a new sorted list and the initial list will not be changed 
#list.sort() will just sort the original list
ages = [10, 8, 23, 40, 35]
la = sorted(ages)
print(la, ages)

n = ages.sort() # this will sort the list in place and return none for the value of n
print(n) # none
print(ages)
# by default things are sorted in ascending order i.e from lowest to highest
# the order can also be reversed 
ages.sort(reverse = True)
print(ages) 
# python returns an error if the element of the list are cannot be sorted 
# i.e it contains a string and an int
l1 = [1, 3, "4"]
# l1.sort() # this will give an error

# max() and min()
l2 = [-9, 10, 5, 100, 66]
print(f'max: {max(l2)}')
print(f'min: {min(l2)}')
print(f'sum: {sum(l2)}')