import random
weather = ['raining', 'sunny', 'cold']
condition = random.choice(weather)
if condition == 'sunny':
    print("wear your glasses")
elif condition == "raining":
    print("take your umbrella")
else:
    print('take your coat along')
