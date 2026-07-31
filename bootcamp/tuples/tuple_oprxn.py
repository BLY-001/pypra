#TUPLE OPERATIONS
my_tuple =(1.4, 10, 'abc', True, (30, 40), 'x')
#tuples can be concatenated just like list and strings
t1 = my_tuple + tuple('yz')
print(t1)
t2 = (1, 2, 'a') * 3
print(t2)
# tuple can also be sliced the same way like string and list
print(my_tuple[0:2])
print(my_tuple[:3])
print(my_tuple[::])
print(my_tuple[::2])
print(my_tuple[::-1])

movies = ('the wizard of oz', 'The Legend', 'Casablanca')
for movie in movies:
    print(f"we are watching {movie}")

    #you can also check for membership in tuple
print("The Legend" in movies)
print('The Legend' not in movies)
