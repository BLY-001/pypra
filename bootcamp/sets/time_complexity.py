# TIME_COMPLEXITY
import time
import sys

# this is to compare the look up time in list and sets
l1 = list(range(1_000_000))
start = time.time() # the time before the lookup

bv = 456789 in l1
end = time.time() #the time after the lookup
print(f'list lookup time: {end - start:.10f}') #time taken to make the lookup
print(f'list memory usage: {sys.getsizeof(l1)}')# this will display the size in byte occuppied by the variable
print("_" * 50)

s1 = set(range(1_000_000))
start = time.time()
bv = 456789 in s1
end = time.time()
print(f'set lookup time: {end - start:.10f}')
print(f'set memory usage: {sys.getsizeof(s1)}')

#from the program we've been able to deduce that sets have negligible lookup time compared to list
# its also noted that list is more memory efficient than sets