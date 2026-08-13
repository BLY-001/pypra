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
    
        
