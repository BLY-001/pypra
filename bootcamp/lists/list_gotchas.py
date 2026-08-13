# PYTHON LIST GOTCHAS
l1 = [1, 2, 3]
l2 = l1 # this doesnt change the memory address it just create a new name for the same memory address
l2[0] = 'xx'
l2.append(10)
print(f'l2: {l2}')
print(f"l1: {l1}") # both l1 and l2 will print out same thing because they are the same
print(id(l1), id(l2)) # l1 and l2 reference thesame memory address
l1.remove(2)
print(f'l2: {l2}') # the value 2 is also removed from l2

#to create a copy of a list use copy()
l3 = l1.copy()
# here l1 and l3 are different lists
l3.append("abc")
print(f'l1: {l1}')
print(f'l3: {l3}')
print(id(l3), id(l1)) # the addresses are different

#2.
nums =[1, 2, 3, 4, 5, 6, 7, 0, 1, 2]

# this is wrong
# for n in nums:
#     if n in nums:
#         nums.remove(n)
# print(nums)
# this will not work because you cannot modify a list while iterarting over it

# the correct way to remove numbers less than 5 is to  create a new list and use append()
new_list = list()
for n in nums:
    if n >= 5:
        new_list.append(n)
print(new_list)

# you can also use list comprehension method

my_list =[n for n in nums if n >= 5]
print(my_list)



