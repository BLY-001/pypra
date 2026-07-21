# # for, else and break statement

# for number in range(10):
#     print(number)
#     if number == 5:
#         break
# print('--------------')
# for number in range (4):
#     if number == 3:
#         print(number)
#         break
# else:
#     print("we've gotten a number")

# for l in "abc":
#     print(l)
#     for n in range(4):
#         if n == 2:
#             break
#     print(n)

for number in range(10):
    print(number)
    if number == 5:
        break
# exit() this stops the entire script
print('outside for')

for letter in 'python':
    if letter == 'o':
        print('letter is o and i\'m braeking out')
        break
    print(letter)

for n in range(1, 12):
    if n % 13 == 0:
        print('there is a number divisible by 13 in the range ... breaking out')
        break
else: #this belong to the for loop(works like an if/else)
    print('there is no number divisible by 13')

for l in "abc":
    print(l)
    for n in range(3):
        if n== 1:
            break
        print(n)