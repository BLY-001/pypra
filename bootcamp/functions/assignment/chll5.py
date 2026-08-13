# Challenge #5
# Using the function defined in the previous challenge find 5 prime numbers greater than 1,000,000
# Are you stuck? Do you want to see the solution to this exercise? Click here.

def check_prime(x):
    if x <= 1:
        return False
    for n in range(2, x):
        if x % n == 0:
            return False 
    return True
primes = []
for n in range(1_000_000, 100_000_000):
    if check_prime(n)== True:
        primes.append(n)
    if len(primes) == 5:
        break
print(primes)