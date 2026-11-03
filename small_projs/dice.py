import random

def roll_dice():
    while True:
        x = input("write your input here (y/n): ").lower()
        if x == "n":
            print('Okay! you can try again!')
            break
        elif x == "y":
        
            number_of_time = int(input("write the number of times to roll the dice: "))
            number_of_dice = int(input("how many dice would you like to roll: "))
        
            round_results = []
            for _ in range(number_of_time):
                rolls = []
                for _ in range(number_of_dice):
                    rolls.append(random.randint(1,6))
                round_results.append(rolls)
            print(round_results)
        else:
            print("invalid character!")  

roll_dice()





















# def roll_dice():
#     counter = 0
#     my_str ="abcdefghijklmn"
#     result_list = []
#     while True:
#         x = input("do you want to play(y/n)? :").lower()
#         num_of_time = int(input("How many times do you wanna roll? "))
#         num_of_dice = int(input("How many dice ? "))
#         validator = 0
#         if x == "y":
#             if num_of_time > len(my_str)/2:
#                 raise Exception(f"cannot handle more than {len(my_str)} dice combination at the moment")
#             while num_of_time < len(my_str)/2:
#                 for item in my_str[:num_of_dice]:
#                     item = random.randint(1,6)
#                     result_list.append(item)
#                 validator += 1
#                 counter += 1
#                 if num_of_time == validator:
#                     print(f"total dice rolled = {num_of_dice}\ntotal number of time it was rolled= {num_of_time}\nthe outcomes are {tuple(result_list)}\nthe total number of rolls is {counter} ")
#                     result_list.clear() 
#                     break
#         elif x == "n":
#             print("okay!, You can try gain anytime!")
#             break
#         else:
#             print("invalid character!, Try Again!")
       
     
# roll_dice()