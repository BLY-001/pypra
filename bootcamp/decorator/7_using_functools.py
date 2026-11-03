# INTROSPECTION USING @functools.wraps() to preserve meta data
import functools
#introspection is the ability of an object to know about its attribute at run time


#if we try to acess the name and documentation of a decorated function,
# it gives the info of the decorator because the decorated function is an argument of the decorator
#so inorder to avert this so that the decorated function can access its name and documentation while
#still an argument of the decorator we will use @functools.wraps() inside the decorator function
# to use functool we will have to import it

user = {"username": "js", "level": "admin"}

def only_admin(func):
    #decorating the wrapper function
    @functools.wraps(func) # this will ensure that decorated functions behave normally an ensures introspection
    def wrapper_only_admin(*args, **kwargs): #the use of *args aand **args means the function returned by the wrapper function can conatain zero or more positional or keyword arguments
        if user["level"] == "admin":
            return func(*args, **kwargs)
        else:
            raise PermissionError("Permission denied") # permission error is a builtin exception and permission denied is the message
            #permission error would be raised if the permission level is not admin
    return wrapper_only_admin

@only_admin # the syntax that automatically binds function below to only_admin
def remove_file(f=None):
    """
    This function removes a file.
    """
    import os, os.path
    if os.path.isfile(f):
        os.remove(f)
        print(f"{f} removed")
    else:
        print(f"file not available")

# without the decorator:
# print(remove_file.__doc__) prints This function removes a file.
# print(remove_file.__name__) prints remove_file

# #with decorator(this print the info of the decorator):
# print(remove_file.__doc__) #None
# print(remove_file.__name__) # wrapper_only_admin

#functool help us set the records straight
print(remove_file.__doc__)
print(remove_file.__name__)
