import random

SCISSORS = "s"
ROCK = "r"
PAPER = "p"

emoji = {ROCK:"🪨", SCISSORS:"✂️", PAPER:"📃"}
choices = tuple(emoji.keys())

def take_input():
    while True:
        guess = input("input your guesse here: ").lower()
        if guess in choices:
            return guess
        else:
            print("invalid")
        

def display_input(guess, computer_choice):        
    print(f"your input is {emoji[guess]}\nthe computer_choice is {emoji[computer_choice]}")


def run_game(guess, computer_choice):
        if computer_choice == guess:
            print("this is a draw")
        elif (computer_choice == ROCK and guess == PAPER 
                or computer_choice == SCISSORS and guess == ROCK 
                or computer_choice == PAPER and guess == SCISSORS):
            print("you win")
        else:
            print("you lose")


def play_rsp():
    computer_choice = random.choice(choices)
    guess = take_input()
    display_input(guess, computer_choice)
    run_game(guess, computer_choice)
    while True:
        retry = input("do you want to play again(y/n)? ").lower()
        if retry == "y":
            play_rsp()
        elif retry == "n":
            break
        else:
            print("invalid the game will terminate")
            break
    

play_rsp()
