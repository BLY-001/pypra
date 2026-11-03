#CREATING AND USING DECORATORS

#by definition a decorator is a high order function that takes another function as an argument
#and extends or decorate the behaviour of the latter function without explicitly modifying it
#also a decorator returns a function

#a usecase is when we have a function that does some simple stuffs and in time we want to add more functionality
#or code to our function

user = {"username":"js", "level": "admin"}

def user_has_permission(func):
    def wrapper_user_has_permission():
        if user["level"] == "admin":
            return func()
        else:
            return None
    return wrapper_user_has_permission




def show_pass(): # this function will show the password
    return "Df1aFgK6j-.,"

my_function = user_has_permission(show_pass)
print(my_function())