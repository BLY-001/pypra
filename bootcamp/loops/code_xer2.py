# x = 0
# my_sum = 0
# while x <= 100:
#     if x % 2 != 0:
#       my_sum += x
#     x += 1
# print(my_sum)

# x = 100
# m = 0
# while x > 0 :
#     x -= 1
#     if x % 2 == 0:
#         continue
#     m += x
# print(m)

my_sum = 0
x = 100
while x:
    if x % 2 != 0:
        my_sum += x
    x -= 1

print(my_sum)