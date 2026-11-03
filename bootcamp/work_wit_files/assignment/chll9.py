# Challenge #9
# Consider this dictionary file.
# Write a Python script that reads the file in a dictionary. 
# The words in the file will be the dictionary keys
# and the length of each word the corresponding values.

with open('American_english.txt', 'r')as file:
    content = file.read().splitlines()
    n_dict = {}
    for lines in content:
        n_dict[lines] = len(lines)
    print(n_dict)