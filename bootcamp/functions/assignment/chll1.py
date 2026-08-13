# hallenge #1
# Write a Python function that takes a list as an argument and returns a new list with unique elements of the first list in the same order.
# Sample List : [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
# Unique List : [1, 2, 3, 4, 5]

def filter(x):
    l = set(x)
    return list(l)

print(filter([1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]))