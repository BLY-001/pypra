# LOOOPS AND RANGES

s = 0
for n in range(101):
    s += n
print(f'the total sum of the range is {s}')

import random
names =["bboo", 'saka', 'foden', 'danladi', 'tosin', 'gbenga', 'olumide', 'looping']
for n in range(3):
    winner = random.choice(names)
    names.remove(winner)
    print(f'the winner for round {n +1} is {winner}')
    print('_________')