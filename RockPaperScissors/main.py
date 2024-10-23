#Sawyer Wood, rock paper scissors proficiency test
import random

humanscore = 0 #fix this and local value stufffffff
computerscore = 0

def loss():
    print("Loss, Bot gets one point.")
    computerscore = computerscore + 1
    print(f"You score is {humanscore} and the bot's is {computerscore}")

def win():
    print("WIN, you get one point.")
    humanscore = humanscore + 1
    print(f"You score is {humanscore} and the bot's is {computerscore}")

while True:
    action = input("rock, paper, or scissors?: ")
    action = action.lower()
    computeraction = random.randint(1,3)

    if computeraction == 1:
        computeraction = "Rock"

    if computeraction == 2:
        computeraction = "Paper"

    if computeraction == 3:
        computeraction = "Scissors"

    print(f"The computer chose {computeraction}")

    if action == computeraction:
        print("Draw, no points")
        print(f"You score is {humanscore} and the bot's is {computerscore}")
    
    if action != computeraction:

        if action in ["rock", "r"] and computeraction == "Paper":
            loss()

        if action in ["rock", "r"] and computeraction == "Scissors":
            win()

        if action in ["paper", "p"] and computeraction == "Scissors":
            loss()

        if action in ["paper", "p"] and computeraction == "Rock":
            win()
    
        if action in ["scissors", "s"] and computeraction == "Rock":
            loss()

        if action in ["scissors", "s"] and computeraction == "Paper":
            win()