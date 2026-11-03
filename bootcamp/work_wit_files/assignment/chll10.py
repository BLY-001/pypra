# Challenge #10
# Consider the dictionary file from the previous challenge.
# Write a Python script that finds the first 100 longest words in the file.
# Tip: See how to get a sorted view of a dictionary.

with open('American_english.txt', 'r')as file:
    content = file.read().splitlines()
    n_dict = {}
    for lines in content:
        n_dict[lines] = len(lines)
    is_sorted = sorted(n_dict.items(), key=lambda items: items[1] , reverse=True)
    print(is_sorted[:100])
        