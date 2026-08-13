# Challenge #4
# Create a function that takes an integer as an argument and returns True if its a prime number and False otherwise.

def check_prime(x):
    if x <= 1:
        return False
    for n in range(2, x):
        if x % n == 0:
            return False    
    return True

# print(check_prime(5))

def is_prime(x):
    # prime = True
    if x <= 1:
        return False
    n = 1
    while n < x // 2:
        n += 1
        if x % n == 0:
            return False
        break
    return True


print(is_prime(5))