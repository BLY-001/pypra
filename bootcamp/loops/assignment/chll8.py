# Challenge #8
# Write a Python script that displays the following pattern from 1 to n where n is entered by the user.
# If the user enters 6 it will display:
# 1
# 22
# 333
# 4444
# 55555
# 666666

# num = int(input("input number: "))
# n = 0
# while n < num:
#     print(n)
#     n += 1
#     while n < num:
#         print(n)
#         n += 1
    
num = input("input your number here: ")
nums = int(num) 
numss = nums + 1
for n in range(1, numss):
    print(str(n) * n)
