def outer():
    msg = "python"
    x = 0
    def inner():
        nonlocal x
        print(f"{msg} is really cool!")
        x +=1
        return x
    return inner

func1 = outer()
print(func1()) # x = 1
func2 = outer()
print(func2()) #x = 2
func3 = outer()
print(func3()) #x = 3

# the reason x is increamenting anytime it is called is because the closure always save the
# last value of x

 
