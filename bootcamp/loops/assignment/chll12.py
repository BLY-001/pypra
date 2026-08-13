# Write a Python script that draws the following pattern using for loops.

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
x = 1
y = 5
while x <= 4:
    print(x * "*")
    x += 1
    while x == 5 and y <= 5:
        print(y * "*")
        y -= 1
        if y == 0:
            break
    

    
        

# for n in range(5):
#     print(n * "*")
#     if n == 5:
#         n -= 1
#         print(n * "*")