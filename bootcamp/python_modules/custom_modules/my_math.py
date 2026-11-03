#we are using this file as a module so we testing it in my_pythonscript.py
a = 10
def my_sum(*args):
    s = 0
    for number in args:
        s = s + number
    return s
if __name__ == "__main__": # this means we want this indented line to run only on when we run this directly here
    print('message printed inside my_math.py')
    s = my_sum(10, 20, 30)
    print(f'sum calculated inside my_math.py is {s}')
#nb: __name__ = "__main__" here in this file
#whenever my_math is imported __name__ = my_math
else:
    print(f'this is the else code')
    print(f'__name__ inside my_math.py is{__name__}')
