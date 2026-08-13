# Challenge #8
# Write a Python program to remove the nth index character from a nonempty string.
n = int(input('input the nth number to be removed:'))
my_str = input('enter the string to slice:')
# removing index 2
s1 = my_str[:n]
s2 = my_str[n+1:]
s3 = s1 + s2
print(s3)