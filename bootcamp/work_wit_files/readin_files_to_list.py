#READING FILES INTO A LIST

#1. f.read().splitlines()
with open('configuration.txt') as f:
    content = f.read().splitlines() 
# the splitlines() returns the entire file content braking at each line boundary in a list
#nb: /n or line breaks are not included in the result in a list
    print(content)

print("_" * 50)

#2. f.readlines()
# this method reads until the end of the file and returns a list containing the lines 
with open('configuration.txt') as f:
    content = f.readlines() #this returns a list with each line as an element with "\n" at the end of it
    print(content)

print("_" * 50)
#3. f.readline() this method returns just only one line and moves the cursor to the next line
with open('configuration.txt') as f:
    content = f.readline()
    print(content)
# nb: there might be an extra space when you write another print(content)  before printing the next line 
# it is caused because the cursor is already on the 2nd line so print() just prints on the third line.
# it can be averted by using print(content, end="")

print("_" * 50)

#4. list(f)
# this will return each line as an item on the list with \n at the back of it
with open('configuration.txt') as f:
    print(list(f))

#5. iterating over a file
with open('configuration.txt') as f:
    for items in f:
        print(items, end='')