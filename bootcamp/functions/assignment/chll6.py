# Challenge #6
# Write a function called fibo that takes an integer greater than 10 as an argument and returns the Fibonacci series between 0 and the function's argument.
# Fibonacci Series: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
# Example: fibo(23) will return 0, 1, 1, 2, 3, 5, 8, 13, 21

def fibo(x):
    a = 0
    b = 1
    k = []
    while a < x:
        k.append(str(a))
        a,b = b, a+b
    return ', '.join(k)

print(fibo(23))