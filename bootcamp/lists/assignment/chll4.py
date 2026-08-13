# Challenge #4
# Write a Python script that finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence (CSV) on a single line.

for n in range(1500, 3201):
    if n % 7 == 0 and n % 5 != 0:
        print(n, end=",")
