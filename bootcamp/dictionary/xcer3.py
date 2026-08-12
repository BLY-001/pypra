money = {
    'bank': 8564.61,
    'paypal': 1998.21,
    'cash': 480,
    'payoneer':250.5
}
tot = 0
for m in money.values():
    tot += m
print(f'the total money is {tot}')

a = sum(money.values())
print(a)