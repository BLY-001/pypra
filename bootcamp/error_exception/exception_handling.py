# EXCEPTION HANDLING TRY, EXCEPT, ELSE, FINALLY

#1.syntax(parsing) errors also known as compile time errors 
#2. exceptions(run-time errors) also known as run-time errors

#this file will teach about how to keep a program running even if there is an exception

try:
    a = int(input('enter a:'))
    b = int(input('enter b:'))
    c = a/b
    print(c)
#this is how it works if an exception occurs on the try block,
#it will just skip the try block and move to the except block and execute whatever is there 
except:
    print('an exception has occured')

x = 10 # all the codes below will execute regardless of the result f the try / except blocks because they outside it
print(x ** x)
print('some other code....')

# -----------------------------------------------
# in this case we want to add the else clause 
try:
    a = int(input('enter a:'))
    b = int(input('enter b:'))
    c = a/b
    print(c)
#this is how it works if an exception occurs on the try block,
#it will just skip the try block and move to the except block and execute whatever is there 
except:
    print('an exception occured')
#this else block will be executed only if the exception block is not excuted which means
# there is no exception, it runs alongside the try block 
else:
    print('No errors')
    print(f'c:{c}')
#there is also a finally block that runs regardless of the outcome of for,except or else block
finally:
    print("Good bye!")

#Another Example
f = open('a.txt', 'w') # this will run without an exception
try:
    f.write('write something to the file')
except:
    print('cannot write to file')
else:
    print('file was written successfully!')
finally:
    print('this code is always executed!')
    if not f.closed:
        f.close()
    print(f'file closed:{f.closed}')
print('some other code ...')