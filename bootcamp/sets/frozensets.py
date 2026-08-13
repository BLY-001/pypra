#FROZENSETS
#frozensets are immutable sets except  being immutable they possess all the properties of a set
#beign immmutable frozensets can be used as keys in dictionaries or as elements in another set or frozenset
fs1 = frozenset({1, 2, 3, 'a', 'b'})
print(fs1, type(fs1))
s1 = 'python is cool'
fs2 = frozenset(s1)
print(fs2)

fs3 = frozenset() #empty frozenset

fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
fs3 = fs1.intersection(fs2)
print(fs3)

#all this operation can also be performed on mix of sets and frozensets
s1 = {4, 10, 20}
result1 = s1.intersection(fs1)
result2 = fs1 - s1
# the type that will be returned  by the result depends on the operand
print(f'result1 type: {type(result1)}') #type set
print(f'result1 type: {type(result2)}') #type frozenset