#PYTHON TUPLES
# tuples just like list are ordered sequence of items. tuples are immutable

t1 = tuple()#declaration of empty using a tuple constructor
t2 = () #normal empty tuple declaration
t3 = (1, 3.4, 'python', True)
print(t3)
t4 = (10) #a tuple with just one element is an integer
#if you want to declare a single element tuple you will add a coma after the element
print(type(t4))
 # a tuple can also be written without a paranthesis
t5 = 6.9, True, 10, 'abc'
print(type(t5))
# you can also make the argument in a list or string to a tuple

t6 = tuple([1, 2, 4, 5])
print(t6)
t7 = tuple('Hello')
print(t7)
l1 = list(t5) 
print(l1)
#to covert a tuple to a list
# indexing also works for tuples too
print(t5[-1])

