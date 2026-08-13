#LIST METHODS
# l1 = list()
# print(dir(l1))
# help(l1.append)

#Adding to the list: append(), extend(), insert()
#append() adds a single element at the nd of the list
#extend() adds all element of an iterable at the end of the list
#insert() inserts an element at a given index or position

l1 = [1, 2.2, 'abc']
#1. list.append()
l1.append(5)
# l1.append(6, 7) error: you cannot add more than one element using append
l1.append([6, 7]) # an element of type list will be added to the l1 list
print(l1)

#2. list.extend()
l1.extend('abc') # each of 'a', 'b' , 'c' will be added into the list

#3. list.insert()
years = [2020, 2022, 2023]
years.insert(1, 2021)# inserts 2021 at index 1
years.insert(len(years), 2024) # this adds 2024 as the last item on the list
print(years) 
years.insert(-1, 2025) # this actualy inserts on the second to the last position
print(years)

#4. list.clear() these clear all the element in the list and return an empty string
years.clear()
print(years)

#5. list.pop() this removes an element from the list and return the element
# if no argument is given it will remove the last element
l2 = [10, 20, 30, 40]
x = l2.pop() # this removes the last element which is 40
print(x)
print(l2)

y = l2.pop(1) # this removes from index 1
print(y, l2)
#l2.pop(100) #error : using an index that does not exist leads to error: pop index out of range

#6. list.remove() this works directly on the values inside the alist not index 
# and it remove only the first ocurrence , unlike pop() it doesnt return the value it remove

l3 =[10, 20, 10, 40]
l3.remove(10)# removes the first occurence of 10
print(l3)
l4 =[10, 20, 10, 40, 20, 20, 'z']
# to remove all occurences of 20 in the list above we use the while Loop
while 20 in l4:
    l4.remove(20)
print(l4)    