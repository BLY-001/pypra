# Challenge #7
# Write a Python program that displays the multiplication table (from 1 to 10) 
# of a specific integer number entered by the user.
# Input: User enters 8
# Output:
num = int(input("multiplication table of: "))
for n in range(1, 11):
    print(f"{num} * {n} = {num * n}")