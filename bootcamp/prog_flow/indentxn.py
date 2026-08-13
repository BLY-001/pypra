balance = 100
price = 50
if balance >= price:
    answer = input('do you want to continue? enter yes or no:').lower()
    if answer == 'yes':
        print("we'll move on")
    elif answer == 'no':
        print("we'll stop.")
    else:
        print('invalid answer')
    new_balance = balance - price
    print(f'you can book the flight and your new balance will be {new_balance}')
else:
        print(f'insufficient funds! please deposit {price - balance}')


