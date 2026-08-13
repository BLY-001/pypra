# Challenge #9
# Define a function that draws a Christmas tree using asterisks (*). The function takes a single argument, which is the height of the tree.
# Example: by calling draw_tree(5) it will display:
# *
# ***
# *****
# *******
# *********

def draw_tree(x):
    for n in range(1, x*2):
        if n%2 !=0:
            print(n * '*')
            print()

draw_tree(5)