import random

def guesse_number():
    auto_guess = random.randint(1, 100)
    attempt = 0
    while True:
        try:
            attempt +=1
            guess = int(input("guesse the number between 1 and 100: "))
            if auto_guess == guess:
                print("Correct")
                print(f"total number of trials is {attempt}")
                break
            elif auto_guess > guess:
                print("too low")
            else:
                print("too high")
        except ValueError:
            print("please enter a valid number")
        

guesse_number()