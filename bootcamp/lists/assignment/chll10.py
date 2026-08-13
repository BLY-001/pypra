# Challenge #10
# Consider a list of words(strings). Write a Python script that generates a list of tuples where the first element of the tuple is the word in the list and the second element is its length.
# Use list comprehension if possible.
# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# Expected Result: [('Python', 6), ('Java', 4), ('C++', 3), ('Golang', 6), ('Solidity', 8), ('Bash', 4)]

sample_list = ['python', 'java', 'c++', 'golang', 'solidity', 'bash']
result = [(c, len(c)) for c in sample_list]
print(result)