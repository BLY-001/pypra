# Challenge #2
# Create a Python script that removes all the elements of a list that are duplicates.
# Are you stuck? Do you want to see the solution to this exercise? Click here.

lt = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'f']
l2 = list()
for item in lt:
    if item not in l2:
        l2.append(item)
print(l2)
