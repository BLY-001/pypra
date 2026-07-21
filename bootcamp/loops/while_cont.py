x = 12
while x < 100:
    x += 1
    if x % 13 != 0: 
        continue
    print(x)

#JUST THINKING OUT LOUD
# secret_number = 9
# guess = int(input('sec num: '))
# while guess != secret_number:
#     print("wrong")
#     guess = int(input('sec num: '))
#else:
#     print('correct')