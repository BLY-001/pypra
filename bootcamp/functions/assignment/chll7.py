# Challenge #7
# Write a function that takes a list as an argument and returns the Equilibrium Index of the list. If there isn't such an index it returns False.
# Equilibrium index: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/
# Are you stuck? Do you want to see the solution to this exercise? Click here.

def equillibrium_index(x):
    for i in range(len(x)):
        if sum(x[:i]) == sum(x[i+1:]):
            return i
    return 'false'

print(equillibrium_index([2, 3, 10, 5]))  