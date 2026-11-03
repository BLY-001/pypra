#THE DECIMAL MODULE CONTEXT AND METHODS
#the context is something that specifies the context that will affect how the decimals will work
#two important properties are the precsion and the rounding
#precision affects arithhmetic operations, there is a current default context or global context and the local context
#i can retrieve the current global context by writing:
import decimal
from decimal import Decimal
decimal.getcontext()
#this uses a default precision represented as prec = 28, rounding = half_even (which means round to the nearest even number)
#we can get just the values of precision by writing
decimal.getcontext().prec #this returns the value of the precision 
decimal.getcontext().rounding #this returns the type of rounding
decimal.getcontext().prec = 8 # this is used to set the precision to 8
decimal.getcontext().rounding = decimal.ROUND_HALF_UP
a = Decimal('1.25')# using the rounding above printing this will give 1.3 rounding to the nearest whole number
b = Decimal('1.35')# using the rounding above printing this will give 1.4 rounding to the nearest whole number

# we will change the rounding to round_half_even which rounds to the nearest even digit
decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN

a = Decimal('1.25')# using the rounding above printing this will give 1.2 rounding to the nearest even number
b = Decimal('1.35')# using the rounding above printing this will give 1.4 rounding to the nearest even number


#by default decimal uses a precision of 28, this means the number of decimal points it uses in arithmetic calculations,
#precsion doesnt affect how many digit it stores, precision only comes to play during arithmetic calculations

a = Decimal('0.12345')
b = Decimal('0.12345')

#Lets display the current context
decimal.getcontext()

#lets change the precision to 2
decimal.getcontext().prec = 2

print(a) #even when the precision is 2 it prints all digits  i.e 0.12345

# nb: precision also do not take effect on normal float
print(0.12345 + 0.12345)

print(a + b) #this will be in precision of 2 because a and b are decimal objects
# nb: precision, rounding and all other properties come into play during arithmetic operation

# we continue to looking into math operations using decimals, thre are many functions defined in the decimal class we can see them by typing
help(Decimal) # This is the decimal class not the module 

# nb: we cannot use with decimals the function defined in maths Module even if its possible its not recommended because if you use the function of math
#module we wil have the same issue with infinite binary expansion and approximation


below is an example

import math
a = Decimal('0.1')
format(a.sqrt(), '.20f') #0.31622776601683793320 recomended

format(math.sqrt(a), '.20f') #0.31622776601683794118