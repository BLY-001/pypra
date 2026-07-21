# RANGES

r = range(2, 10)
print(type(r))
print(r)
print(list(r))

# range( start, stop, step)

print(list(range(0, 11, 2))) # numbers divisible by 2 between 0 and 10
print(list(range(0, 40, 7))) # numbers divisible by seven between 0 and 39
s = sum(range(0, 1001))
print(s)

# summary 
# 1. range(stop)
print(list(range(10))) # range(0, 10, 1)

#2. range(start, stop)
print(list(range(3, 9))) # range(3, 9, 1)

#3. range(start, stop, step)
print(list(range(5, 100, 13)))

# negative numbers can also be used
print(list(range(-20, 10, 4)))
print(list(range(10, -2, -3)))
