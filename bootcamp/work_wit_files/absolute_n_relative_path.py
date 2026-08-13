#ABSOLUTE AND RELATIVE PATHS
# a relative path is expected to find the file in th current directory
# an absolute file type is defined by specifying the location of the file or directory from the root directory
# f = ('settings.txt')
# below is an absolute path to the settings.txt file
f = open('/home/binlawal/pypra/bootcamp/work_wit_files/settings.txt')

#it is not as easy as this in a linux or mac operating system the paths uses backward slash
# f = open('C:\users\ad\pycharmproj\bootcamp\settings.txt') # htis will result in an error
# to avoid the error we use r-string or we double all the back slash
# f = open(r'C: \users\ad\pycharmproj\bootcamp\settings.txt') # htis will result in an error

#a relative path is the path related to the current working directory it begins with your current directory, no slashes
# a relative path use a single dot "." to represent that the file is in the same directory  i.e current working directory and it can be written as open('settings.txt') or using the "." open(./settings.txt) its still dsame
# a relative path use a double dot ".." to represent that the file is in the parent directory of the current file i.e open(../settings.txt)
