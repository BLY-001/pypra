# Challenge #4
# Write a Python script that tests if a string is a palindrome.
my_str = 'malam'
s = my_str[::-1]
print(my_str == s)

s1 = 'eve'
print(f'is {s1} a palindrome:{s1 == s1[::-1]}')

#ch5

s2 = 'nurses run'
s2 = s2.replace(" ", "")
print(f'answer if {s2} is a palindrome: {s2 == s2[::-1]}')

#Palindrome are strings that reads the same forward nd backwards
