#PROJECT FILE RENAMING AUTOMATION USING SYS AND OS MODULE

import os
#we want to automate the renaming of some multiple files in a directory
os.chdir("/home/binlawal/dir1") #we use this to change to the directory we want to work on
i = 1
for file in os.listdir():
    file_name, file_extension = os.path.splitext(file) # os.path is a submodule that does common pathname manipulations infact it will return a tuple that contain two elements the name of the file and its extension
    # because the name of the file will be without extension to confirm let print both variables
    # print(file_name, file_extension)
    new_name= f"{i}-{file_name}{file_extension}"
    i += 1
    # print(new_name)
    # os.rename(oldname, new_name)
    os.rename(file, new_name) # this will rename the file into the new name