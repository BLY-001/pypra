# Challenge #2
# Create a Python script that reads a text file into a list and then converts the list into a string that has the entire file content.

with open('chll2.txt', 'r') as file:
    content = file.readlines()
    str_cont = ''.join(content)
    print(str_cont)
