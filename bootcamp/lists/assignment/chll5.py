# Challenge #5
# Write a program that prompts the user for a long string containing multiple words separated by whitespaces and prints back the same string with the words in backward order.
# For example, say I type the string: My name is Andrei
# Then the script should print out: Andrei is name My

input_sentence = input("write your input: ")
script = input_sentence.split()
script.reverse()
# print(script)
rversed = " ".join(script)
print(rversed)



