set1 = {'a', 'b', 'c'}
set2 = {'c', 'd', 'e'}
set3 = set1.union(set2)
print(set3)
set4 = set1.intersection(set2)
print(set4)
set5 = set1.difference(set2)
print(set5)
set1.discard('c')
print(f'new set1: {set1}')