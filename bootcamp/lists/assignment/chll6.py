# Challenge #6
# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample input string : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

input_str = input("put your string: ")
input_list = input_str.split("-")
input_list.sort()
sorted_res = "-".join(input_list)
print(sorted_res)
