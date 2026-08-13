# Challenge #7
# Write a Python program that accepts as input a sequence of words separated by one or more whitespaces and prints out the same words with the letters in reversed order. Do not use list comprehension.
# Sample input string: I love cat and dogs
# Expected Result: I evol tac dna sgod

inpuy = input("input: ")
listed = inpuy.split()
rsult = [c[::-1] for c in listed]
print(f"{" ".join(rsult)}")

# g = "i love cat and dogs"
# print(g[::-1])
