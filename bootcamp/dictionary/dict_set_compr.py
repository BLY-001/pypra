#SET AND DICT COMPREHENSIONS
#The syntax is same the syntax for list comprehension just that we use {curly braces} in this regard

#set comprehension
names = {'tom', 'ANNE', 'jOhn', 'dAn' }
names = {n.capitalize() for n in names}

#dict comprehension

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {k*2: v*2 for k,v in d1.items()}
print(d2)

d3 = {k.upper(): v*2 for k, v in d1.items()}
print(d3)

#using zip() this takes one or more iterable as argument and aggregrate them into a zip object
# which is another iterator of tuples this iterator can be transformed into
# a list of tuples or a dictionary
years = [2017, 2018, 2019]
revenues = [3000, 40000, 50000]
z = zip(years, revenues)
sales = list(z)
print(sales) #list of tuples
#if we want a dictionary we will use a dict constructor
my_sales = dict(zip(years, revenues)) #NB: the zip file cannot be used twice hence thats why we use zip(years, revenue) instead of using varible z
print(my_sales)
# if the iterable passed as argument to the zip() is of different lenght the shortest length decide the length for the new iterable
# year = [2017, 2018, 2019, 2020, 2021]
# revenue = [3000, 40000, 50000]
# y = zip(year, revenue)
# sales = list(z) #th length of the list is 3 cos its the length of the shortest arg

#to know the profit in my_sales
profit = {k: v*0.15 for k,v in my_sales.items()}
print(profit)