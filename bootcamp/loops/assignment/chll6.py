# Challenge #6
# Given the string s1, write a program to return the sum and the average of the digits that appear in the string, ignoring all other characters.
# Input: Python31py50
# Output: Sum: 9, Average: 2.25
# s1 = "Abcde1234svdg"
s1 ="Python31py50"
# s2 = (s1[6:8] + s1[-2:])
# s3 = int(s2)
# length = len(s2)
sum = 0
count = 0
# average = 0
for n in s1: # this loops through all iteration of the strings stored in s1 
    if n.isdigit(): #this checks if any of the alphabets is a digit
        count += 1
        sum += int(n)
    if count >= 1:
        average = sum/count
print(f"sum: {sum}, average:{average}")
