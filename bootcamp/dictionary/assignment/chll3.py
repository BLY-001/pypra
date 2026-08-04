# Challenge #3
# Considering the following dict, get a dict representation sorted by key.
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# A dict representation means viewing or printing the dict.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
d2 = list(d1.items())
sorted_list = sorted(d2)
sorted_dict = dict(sorted_list)
print(sorted_dict)

#loop solution
s1 = dict()
d3 = sorted(d1)
for items in d3:
    s1[items] = d1[items]
print(s1)

#using dict comprehension
result ={items:d1[items] for items in d3}
print(result)

    
