#Sawyer Wood, Number Guessing Game Raid.

import random #Import random so you can generate random numbers

Goal = random.randint(1, 10) #Generating the random number

Guess = int(input("What to do you think the number is, it is between 1 and 10?: ")) #Getting their guess


while True: #Forever loop

    if Guess > Goal: #If their guess was too high
        print("Your guess was too high, try again.") #Print it was too high
        Guess = int(input("What to do you think the number is, it is between 1 and 10?: "))#Getting their guess

    if Guess == Goal: #If they guess right
        print("You guessed the right number!") #Print they guessed right
        break #Stop the program

    if Guess < Goal: #If their guess was too low
        print("Your guess was too low, try again.") #Print it was too low
        Guess = int(input("What to do you think the number is, it is between 1 and 10?: "))#Getting their guess