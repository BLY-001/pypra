#Challenge #1
# Create a Python script that removes all the occurrences of a given element of a list.
# Are you stuck? Do you want to see the solution to this exercise? Click here.

lt = ['a', 'b', 'c', 'd', 'e', 'a', 'c', 'f']

writen = input("input your element here: ")
l2 = []
for item in lt:
    if item != writen:
        l2.append(item)
print(l2)

while writen in lt:
    lt.remove(writen)
print(lt)