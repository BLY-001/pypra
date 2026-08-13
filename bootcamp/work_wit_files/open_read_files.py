#WORKING WITH FILES
#OPENING AND READING FILES

# type of files 
# 1. text Files
# 2. binary files

# f = open("file name", access mode)
# open() is a built in function that opens a file and return a file object
# f is the file object and it c
# 'r' means read only and its the default acess mode for opening a file
# 't' means to open it in text mode and 'b' means to open it in binary mode
f = open('configuration.txt', 'rt')
content = f.read() # calling a method on the file object
print(content)
f.close() # this method is used to close the file object
print(f.closed) # this used to confirm the status TRUE means the file is closed false means its open