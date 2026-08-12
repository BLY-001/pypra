# challenge #13
# Consider the two Python lists. 
# Write a Python Script to make a new list whose elements are the intersection of the two given lists.
# This means all elements of L1 that also belong to L2, but no other elements.

l1 = ["Dan", "John", "Diana"] 
l2 = [11111, 2222, 3333, 'Dan']

new_list = set(l1) & set(l2)
print(list(new_list))