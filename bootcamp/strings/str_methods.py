#string methods

# builtin functions print(), len(), type(), sum(), max(), min(), round()

# we can use print(dir(type)) to display all methods of any data type i.e str,int, float etc
# we can use help() to make enquiries i.e help(str.replace)

# to call a method we use thr dot '.' notation
s = 'python'
s.upper()
print(s) #python unchanged because strings are immutable
new_s = s.upper()
print(new_s) #PYTHON

print('prOgrammING'.lower()) # we can also call the method directly on the string 

#more on python method
my_str = 'I learn python Programming'

# 1. str.upper()
print(my_str.upper()) #changes all of my_str to uppercase letters

#2. str.lower()
print(my_str.lower()) #changes all of my_str to lowercase letters

#3. str.strip()
ip = '  192.167.0.1    '
ip = ip.strip() # in this case strip is used to remove spaces in front and back of the ip adrress
print(ip)
value = '$$200$$$'
print(value.strip('$')) # this removes $ from the string

#4. str.replace()
new_value = value.replace('$', '#') # this aims to remove  particular cahracter with another
print(new_value)

# 5. str.count()
txt = 'I learn python , python is cool!'
n = txt.lower()count('python')
print(n)
print(txt.count('y'))

#6. str.split()
my_list = txt.split() # this automatically split a string into a list using space 
print('10.1.2.3'.split('.'))

# 7. str.join() 
#this is the opposite of split it converts directly from list back to strings
ip = '10.1.2.3'
ip_list = ip.split('.')
print(ip_list)

ip_str = '.'.join(ip_list)
print(ip_str)


# 8. str.find()
my_str = 'i learn python programming'
print(my_str.find('python'))# this will show 8 which is the index of the first occurence of python
# if the string isnt present it will return -1

#in
print('golang' in my_str) #false
# this is more useful to check if a particular string is present

#not in
print('golang' not in my_str)