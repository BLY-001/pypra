# READING FILES, TELL(), SEEK() AND CURSOR

f = open('configuration.txt')
#the read method can take a second optional argument called size which is an integer that indicates how many characters to read from the file
content = f.read(5) # to read only the first 5 characters of the file
print(content)
# the first read(5) means the curson is now after the fifth character
content = f.read(3) #this will read another 3 from cursor 5
print(content)

# we can get the position of the curson by using the tell method
print(f.tell())

#to move to a particular position in the file we use seek() method
f.seek(0)# this will move the cursor to the beginning of the file 
content = f.read(3)
print(content) # this will print the first 3 charcters of the file

