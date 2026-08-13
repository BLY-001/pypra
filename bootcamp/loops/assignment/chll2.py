# Challenge #2
# Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.
# Input: 16, 2
# Output: 2 ** 4 = 16
x, y =int(input("input the value of x")), int(input("input the value of y"))
result =0
while result < x:
    result += 1
    if y ** result != x:
        continue
    print(f'input: {x}, {y}')
    print(f'output: {y} ** {result} = {x}')    

        
