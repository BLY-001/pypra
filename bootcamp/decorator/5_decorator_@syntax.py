#THE @SYNTAX DECORATOR

#the function of the code below is to remove a file if the user has admin level

user = {"username": "js", "level": "admin"}

def only_admin(func):
    def wrapper_only_admin(*args, **kwargs): #the use of *args aand **args means the function returned by the wrapper function can conatain zero or more positional or keyword arguments
        if user["level"] == "admin":
            return func(*args, **kwargs)
        else:
            raise PermissionError("Permission denied") # permission error is a builtin exception and permission denied is the message
            #permission error would be raised if the permission level is not admin
    return wrapper_only_admin

# def remove_file(f=None):
#     import os, os.path
#     if os.path.isfile(f):
#         os.remove(f)
#         print(f"{f} removed")
#     else:
#         print(f"file not available")

# #we can also catch the permission error while running the program by using try and except blocks
# try:
#     remove_file = only_admin(remove_file)
#     remove_file("a.txt")
# except PermissionError as e:
#     print(e) # e is the message in the exception raised above


#USING THE @ SYNTAX
#instead of always calling the onlyadmin() function with the remove_file
#we can constantly call the remove_file() function alone because the @syntax will parmanently attach both and automatically assign it to 
#remove_file such that when we call it we get the same result as above
#  BELOW IS A CLEAR EXAMPLE

# @ or pie syntax
@only_admin # the syntax that automatically binds function below to only_admin
def remove_file(f=None):
    import os, os.path
    if os.path.isfile(f):
        os.remove(f)
        print(f"{f} removed")
    else:
        print(f"file not available")

#so you can just call remove file and the result will be same
try:
    remove_file("a.txt")
except PermissionError as e:
    print(e)
