# Challenge #10
# Write a Python program that iterates over the integers from 1 to 50.
# For multiples of three print "Foo" instead of the number and for multiples of five print "Bar".
# For numbers that are multiples of both three and five print "FooBar".

for n in range(1,51):
    if n % 5 == 0 and n % 3 == 0:
        print(f"{n}. FooBar")
    if n % 3 == 0:
        print(f"{n}. Foo")
    if n % 5 == 0:
        print(f"{n}. Bar")
    