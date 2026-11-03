# Challenge #1

# Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number less than the asked number.

a = int(input("input your number:"))
a -= 1
while a >= 1:
    divisor = []
    b = a
    while b >= 1:
        if a % b == 0:
            divisor.append(b)
            # print(divisor)
        b -= 1 
    print(f"the divisors of {a} are {divisor}")
    a -= 1

#LATER GOT A SECOND SOLUTION

# number = int(input("input number here: ")) - 1
# divisiors = []
# while number > 1:
#     for num in range(1, number + 1):
#         if number % num == 0:
#             divisiors.append(num)
#     print(f"the divisiors of {number} are {divisiors}")
#     divisiors.clear()
#     number -= 1

        
