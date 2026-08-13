import random
lights =['red', 'yellow', 'green']
color = random.choice(lights)
if color == 'red':
    print('stop')
elif color == 'yellow':
    print('prepare to stop')
elif color == 'green':
    print('Go')