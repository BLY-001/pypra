#LIST COMPREHENSION THAT INCLUDES IF STATEMENT
# [EXPRESSION FOR ITEM IN ITERABLE IF STATEMENT]

nums = [1,7,8,14,21,23,50]
div_by_seven = [n for n in nums if n % 7 == 0]
print(div_by_seven)

num_str = [str(n) for n in nums]
print(num_str)
# to convert back to string
"-".join(num_str)
print(num_str)

friends = ['john', 'dan', 'marry']
neighbors = ['tim', 'steve', 'dan', 'john']
# we want to create a list that has both friends and neigbor
friends_and_neighbors = [name for name in friends if name in neighbors]
print(friends_and_neighbors)

# if their are name with mixed case letters the above methods will not work
# friends  = ['JOHN', 'Dan', 'marry']
# neighbors = ['tim', 'steve', 'DAN', 'john]

friend_lower = [name.lower() for name in friends]
fn = [name for name in neighbors if name.lower() in friends]
print(fn)

