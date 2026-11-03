# Challenge #6
# Write a Python program to count the number of lines, words, and characters in a text file.
# This is similar to the Linux `wc` command. Create a function, if possible.

def countlines(name):
    with open(name, 'r')as f:
        content = f.read().splitlines()
        d = len(content)
        r = f"the count of lines is {d}"
    with open(name, 'r') as file:
        content = file.read().split()
        s = f'the count of words is {len(content)}'
    with open(name, 'r')as f:
        content = f.read()
        t = f'the count of characters is {len(content)}'
        return r,s,t

print(countlines('chll2.txt'))