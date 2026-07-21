x = 0
while x < 10:
    print(f'the current value of x is {x}')# if left here the code becomes an infinit loop
    x = x + 1 # or x += 1
else:
    print(f'finishing printing numbers x is now {x}')

# SORRY JUST THINKING OUT LOUD
# for l in range(1, 5):
#     if l == 5:
#         print(f'the number is {l}') 
#         break
# else:
#     print('the number is invalid')
