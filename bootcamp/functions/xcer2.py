x = 10
def increment():
    global x
    x += 1
    return x

print(increment())