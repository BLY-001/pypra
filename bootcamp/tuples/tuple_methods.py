#TUPLE METHOD
t1 = (1, 2, 1, 3, 4)
#1. tuple.index()
i = t1.index(2)
print(f"2 is at position {i}")
#if the value you entered is not inside the tuple 
# you will get Value error
#i = t1.index(x) #ValueError
x = 10
if x in t1:
    i = t1.index(x)
    print(f'x at index {i}')
else:
    print(f'{x} not in tuple')

#2. tuple.count() #this return the index of the first occurence of an element
n = t1.count(1)
print(n)

# built in fucntions like len(), sum(), min(), sorted() works with tuple
print(len(t1))
print(sum(t1))
print(max(t1))
print(min(t1))

t2 = sorted(t1) #ascending order
# t2 = sorted(t1, reverse=True) #descending order
print(t2)
