# Challenge #4
# Considering the following dict, get a dict representation sorted by value.
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# A dict representation means viewing or printing the dict.

d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
d2 = d1.items()
l1 = list(d2)
l4 = []
for items in l1:
    l3 = items[::-1]
    l4.append(l3)
l5 = dict(sorted(l4))
dicto = {}
for k,v in l5.items():
    k, v = v, k
    dicto[k] = v
print(dicto)
# line 19-21 can be written better as
for v, k in l5.items():
    dicto[k] = v
print(dicto)

#Considering the following dict, get a dict representation sorted by key.
# A dict representation means viewing or printing the dict
d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
view = sorted(d1.items(), key = lambda items: items[1])
print(view)
