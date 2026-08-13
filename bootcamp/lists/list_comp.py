#LIST COMPREHENSION
clicks = [10, 5, 15, 20]
doubled_list = list()
for c in clicks:
    doubled_list.append(c*2)
print(doubled_list)

#using list comprehension
# [expression for item in iterable]
doubled_numbers = [c *2 for c in clicks]
print(doubled_numbers)

name = "andrei"
l1 = [char for char in name]
print(l1)

l2 = [char * 3 for char in name]
print(l2)

l3 = [(char * 3).upper() for char in name]
print(l3)

friends = ["andrei", "diana", "paul", "mary"]
my_friends = [item.capitalize() for item in friends]
print(my_friends)

reversed_names = [item[::-1] for item in friends]
print(reversed_names)

