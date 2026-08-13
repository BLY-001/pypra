# Challenge #7
# Write a Python program that accepts as input a sequence of words separated by one or more whitespaces and prints out the same words with the letters in reversed order. Do not use list comprehension.
# Sample input string: I love cat and dogs
# Expected Result: I evol tac dna sgod

n_input = input('input your string: ')
n_list = n_input.split()
n_list.reverse()
n_str = " ".join(n_list)
print(n_str[::-1])

#method 2
c = []
for i in n_list:
    c.append(i[::-1])

print(f"{" ".join(c)}")