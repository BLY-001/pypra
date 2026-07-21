# secret_num = 9
# guess = int(input('write your secret number'))
# while guess != secret_num:
#     print('you loose')
#     guess = int(input('write your secret number'))
#     print('you won')

# while True:
#     guess = int(input('netr oo:'))
#     if guess == 7:
#         print('you won')
#         break
#     print('you loose')

a = int(input('eneter num: '))
while a > 1:
    b = a // 2
    while b > 1:
        if a % b == 0:
            break
        b -= 1
    else:
        print(f'{a} is prime')
    a -= 1