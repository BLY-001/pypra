#VARIABLE LENGTH ARGUMENTS (*args)

# *args : sometimes you do not know how many argument a function should take and you want to call it with a variable number of arguments
def average(a, b, *args):
    # print(f'args is {args}')
    return (a + b + sum(args)) / (2 + len(args))
# *args where args is infact a tuple of potential additional arguments this tuples is initially empty which means you do not get any error if you do not specify any additional argument when calling the function

def concatenate(*args):
    result = ''
    for tmp in args:
        result += tmp
    return result

r = concatenate("python", " 3", "!")
print(r)
result = concatenate('I', 'Love', 'Programming')
print(result)

# it is not mandatory to use the word *args it could be *x or *y or *anything but it is just standard to use *args


print(average(4, 5, 6, 7 ))

