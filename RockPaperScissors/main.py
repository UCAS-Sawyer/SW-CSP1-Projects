#Sawyer Wood, rock paper scissors proficiency test

import random

humanscore = 0
computerscore = 0

array1 = {
    "r": "rock",
    "p": "paper",
    "s": "scissor"
}

def loss():
    print("Loss, Bot gets one point.")
    print(f"Your score is {humanscore} and the bot's is {computerscore}")

def win():
    print("WIN, you get one point.")
    print(f"Your score is {humanscore} and the bot's is {computerscore}")

moves= ["r", "p", "s"]


while True:
    action = input("rock, paper, or scissors?: ")
    action = action.lower()

    computeractionchoice = random.choices(moves)
    computeraction = computeractionchoice[0]

    if action == "q":
        print("Done")
        break

    if action not in moves:
        print("You can only try 'r' 'p' 's' or 'q'")
        continue
    
    print(f"\tThe computer chose {array1[computeraction]}")

    if action == computeraction:
        print("Draw, no points")
        print(f"Your score is {humanscore} and the bot's is {computerscore}")
        continue
    
    elif action != computeraction:

        if action == "r" and computeraction == "p":
            computerscore += 1
            loss()

        if action == "r" and computeraction == "s":
            humanscore += 1
            win()

        if action == "p" and computeraction == "s":
            computerscore += 1
            loss()

        if action == "p" and computeraction == "r":
            humanscore += 1
            win()
    
        if action == "s" and computeraction == "r":
            computerscore += 1
            loss()

        if action == "s" and computeraction == "p":
            humanscore += 1
            win()