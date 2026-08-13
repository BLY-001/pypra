# Write a Python script that prints out the Fibonacci series up to a given number n.
# Fibonacci Series: https://www.mathsisfun.com/numbers/fibonacci-sequence.html
# Example: if n is 23 it will print out 0, 1, 1, 2, 3, 5, 8, 13, 21
n = int(input("input : "))
i = 0
j = 1
a = []
while i < n:
    a.append(str(i))
    i, j = j, i + j
a = ", ".join(a)
print(a)