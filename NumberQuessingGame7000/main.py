#Sawyer Wood, Number Guessing Game Raid.

import random

Goal = random.randint(1, 10)

Guess = int(input("What to do you think the number is, it is between 1 and 10?: "))


while True:

    if Guess > Goal:
        print("Your guess was too high, try again.")
        Guess = int(input("What to do you think the number is, it is between 1 and 10?: "))

    if Guess == Goal:
        print("You guessed the right number!")
        break

    if Guess < Goal:
        print("Your guess was too low, try again.")
        Guess = int(input("What to do you think the number is, it is between 1 and 10?: "))