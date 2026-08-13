# Challenge #3
# Write a function that returns the factorial of a number n which is the function's argument.
# Factorial: https://en.wikipedia.org/wiki/Factorial

def factorial(x):
    for n in range(1, x):
        x *= n
    return x

print(factorial(5))
