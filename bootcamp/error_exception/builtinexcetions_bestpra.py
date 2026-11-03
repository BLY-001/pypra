#BUILT-IN EXCEPTIONS AND BEST PRACTICES
#there are sevral classes of built in error in python
#ther are more accurate ways of catching exceptions in python and it is what we are about to learn in this file
# best practice is to create multiple except clauses according to your application scenerio

try:
    a = int(input('enter a:'))
    b = int(input('enter b:'))
    d = 7
    c = a/b + d
except ZeroDivisionError as e: #here we are specific about the kind of error we want our exception to catch
    print(f'division by zero is not permitted:{e.args}')
except TypeError as e:
    print(f'opertions of different types are not permitted:{e}')
except:# this is the generic exception block that will catch any other exception
    print(f'a generic exception has occured: {e}')
else:
    print('No errors')
    print(f'c:{c}')
finally:
    print('Good bye!')

# we want to write a code that will continue asking for numbers until there is no exception
# all we just have to do is to use an infinite while loop and break once the answer is correct

while True:
    try:
        a = int(input('enter a:'))
        b = int(input('enter b:'))
        d = 7
        c = a/b + d
    except ZeroDivisionError as e: #here we are specific about the kind of error we want our exception to catch
        print(f'division by zero is not permitted:{e.args}')
    except TypeError as e:
        print(f'opertions of different types are not permitted:{e}')
    except:# this is the generic exception block that will catch any other exception
        print(f'a generic exception has occured: {e}')
    else:
        print('No errors')
        print(f'c:{c}')
        break #the else block executes once their is no exception so its normal to break once the else block is executed the finally block will execute regardless
    finally:
        print('Good bye!')

#you can also raise your own exception using the raise keyword
age = -1
if age < 0:
    raise Exception('age below zero is not permitted!')
