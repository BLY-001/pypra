balance = 100
price = 50
if balance >= price:
    new_balance = balance - price
    print(f'you can book the flight and your new balance will be {new_balance}')
else:
    print(f'insufficient funds! please deposit {price - balance}')

# print('no instruction')
