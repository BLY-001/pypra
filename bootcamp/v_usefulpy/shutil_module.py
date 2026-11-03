#SHUTIL(SHell UTILity)
# HIGH-LEVEL FILE OPERATIONS
  
# this module offers a number of high-level operations on files and directories
# such as copying,moving, renaming or deleting some file operations can also be done using the OS module
# but many python programmers prefer to use shutil because it hides the complexity of the operation, shutil functions are built on top of OS modules
# and each call may represent alot of other calls to lower level functions 

import shutil #importing shutil module
# copyfile copies the content of the file from a file named source file to a file named destination file, source file and destination file are valid path names
# given as strings this only copies the content of the file other metadata like the files permisions mode the files creationa nd modification time are not preserved
# shutil.copyfile("/home/binlawal/a1/file1.txt", "/home/binlawal/b2/file3.txt")
# shutil.copy("/home/binlawal/a1/file1.txt", "/home/binlawal/b2")#this copies the files data and the file permision modes other metadatas like the file mdoification time and creation time are not preserved
# shutil.copy2("/home/binlawal/a1/file1.txt", "/home/binlawal/a1/file2.txt") # this is identical to copy just that it attempts to preserve all permisions and metadatas like files creation and modification times 
# # nb: even copy2 cannot preserve all metadata, on windows, linux and mac info like file owner and acs are not copied

# #if you want to copy an entire directory use the copytree function, i.e shutil.copytree() it recursively copies an entire directory tree,
# #the destination directory must not already exist, it will be created as well as missing parent directories, permisions and time of directory are copied with copystart() function,
# #and individual files are copied using copy2() function 
# shutil.copytree("/home/binlawal/a1", "/home/binlawal/b2/c") #to copy the directory called "a" into the directory called b as c


#another important function is move() it recursively moves a file or directory to another location
#if the destination is an existing directory then the source is moved inside that directory
#and if the source and the destination are in the same dirctory the source is renamed

# shutil.move("/home/binlawal/a1", "/home/binlawal/x")# this will rename the a1 directory to x
# shutil.move("/home/binlawal/x", "/home/binlawal/b2")# this will move the x directory into b2 directory

# shutil.rmtree( "/home/binlawal/b2") #is used to delete an entire directory tree in this case we delete b2