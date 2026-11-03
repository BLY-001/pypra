#DECIMAL ARITHMETIC AND DECIMAL MODULE
#in this lecture we will see how to avoid a very serious problem we have with float
#some rational numbers cannot be represented using a finite number of digits
#i.e 1/3 is a finite number with an infinite number of decimal digits
# we use the built-in format() function to set the number of decimal points we want to display

format(1/3, '.24f') #this will format it to 24 decimal points
format(1/3, '.5f') #this will format it to 5 decimal points
# numbers in a computer are represented using bits not decimal digits so instead of power of 10(base 10) it uses power of 2(base 2)
#the same problem that occurs when trying to represent 1/3 also happens when trying to represent certain float numbers using the binary system, this is caused by what is called infinite binary expansion and its not a python issue-
#its infact its a problem of any other programming language, one very simple examplle is when trying to represent  0.1 or 0.3 python will approximate their representation in binary, they are not finite numbers in binary they are infinite series 
# to show that float numbers are infinite series see the example below
format(0.1, '.25f') #this will format 0.1 to 25 decimal points showing approximated numbers
#however some decimal numbers have a finite binary representation and that means an exact float representation for example 0.125, 1/8 etc
#an infinite binary representation means an approximate float representation 
a = 0.1
b = 0.3
a * 3 == b #false, this returned false because of the infinite binary expansion a * 3 is not equal to b
#what is important is to know how to write code to avoid serious bugs, imagine what happens if a banking application cannot represent 30cents or 0.3dollars and should approximate it
#like finance and banking there are many other fields where exact finite representation are highly desirable 
#best practice when working with floats and equality testing is to use math.isclose() function 

import math
help(math.isclose)


import decimal #this module offers an alternative to using the float type and avoids the approximation issues we have with floats 
#below are some examples
# instead of using decimal.Decimal() we can just import the Decimal class directly from the module
from decimal import Decimal
a = Decimal('0.1')
#IF we want to use a float it is recommended to use a string as shown above 
#we can always use integers directly
a = Decimal(4)

 
