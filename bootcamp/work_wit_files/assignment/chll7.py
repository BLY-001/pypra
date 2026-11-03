# Challenge #7
# Write a Python program that calculates the net amount of a bank account based on the transactions that are saved in a text file.
# The file format is as follows:
# D:50
# W:100
# D means deposit while W means withdrawal.
# Suppose that the following file is supplied to the program:
# D:300
# D:300
# W:500
# D:200
# Then, the output should be: 300

def sum(n):
    amount = 0
    with open(n, 'r') as f:
        for lines in f:
            content = lines.strip().split(':')
            if content[0] == 'D':
                amount += int(content[1])
            elif content[0] == 'W':
                amount -= int(content[1])
        return amount
            
            

print(sum('amt.txt'))