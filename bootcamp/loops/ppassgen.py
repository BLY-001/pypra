# this is a password generator that generates password based on the length you want or input
import random
import string

var1 = string.ascii_letters + string.digits + string.punctuation
length = int(input('input pasword length: '))
password = ''
for _ in range(length):
    c = random.choice(var1)
    password += c
print(password)

#i,m still not able to control the error it will bring if a non int number is inputed