# Challenge #4
# Considering the following dict, get a dict representation sorted by value.
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# A dict representation means viewing or printing the dict.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
#
result ={k:sorted(v) for k, v in d1.items()}
print(result)

value.strip().lower().replace(' ', '_')

