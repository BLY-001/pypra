#WRITING TO TEXT FILES
# to write to a file we call the write() method which writes a string to the txt file
# open('filename', 'access_mode')
# nb: using 'w' (write) as the access mode overwrite the file or creates a new one if it doesnt exist
with open('myfile.txt', 'w') as f:
    f.write('just a line.\n') # f.write('just a line\njust a 2nd line.')
    f.write('just a 2nd line.\n') 
# if there is an existing file and we want to append it not overwrite we can change the acces mode to 'a'(append())
with open('myfile.txt', 'a')as f:
    f.write('Some text here.\nAnother text')

#we can also use r+ for as acess mode
#in this case anything we write will be added at line 1
with open('myfile.txt', 'r+') as f:
    f.seek(5) # this will move the cursor to caharacter 5
    f.write('100') # this will wrrite 100 after character 5
    f.write('Line added with r+\n')
#nb : when using r+ the file must already exist otherwise it will raise an error
# if you want to add an item to any position you can just move the cursor to the position
# with open('myfile.txt', 'r+') as f:
    # f.seek(5) # this will move the cursor to caharacter 5
    # f.write('100') # this will wrrite 100 after character 5
    f.seek(10)
    print(f.read())