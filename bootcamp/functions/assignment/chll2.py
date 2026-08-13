# Challenge #2
# Write a Python function to check whether a number is perfect or not. The function should return True if the number is perfect and False otherwise.
# Perfect numbers: https://www.britannica.com/science/perfect-number

def perfcheck(x):
    c = 0
    for n in range(1, x):
        if x % n == 0:
            c += n
    if c == x:
        return True
    else:
        return False

print(perfcheck(28))