# this is a password generator that generates password based on the length you want or input
import random
import string

Characters = string.ascii_letters + string.digits + string.punctuation
password = ''
try:
    length = int(input('input pasword length: '))
    for _ in range(length):
        c = random.choice(Characters)
        password += c
    print(password)
except ValueError:
    print("invalid input")

    
