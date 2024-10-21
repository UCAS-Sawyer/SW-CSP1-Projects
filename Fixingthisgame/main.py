#Sawyer Wood, fix the game raid.

#This is the code im fixing:
import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 1 #3. Since this starts at one you will get one more guess than max_attempts. Logic error. If you start counting from 0 - 10 there is 11 numbers not 10.
    #To fix 3. just make attempts 1
    game_over = False
    while not game_over:

        guess = int(input("Enter your guess: ")) #The fix for 1. is to just make this an int.

        if attempts >= max_attempts: #2. attempts is not going up so you will never hit this condition. Logic error. The condition will never work, becauseattempts will never be higher than max attempts.
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
            break #4. if this condition happens it will print everything, but keep going downt he list of conditions, which means that the other conditions will still print. Logic error. It just makes the ending wierd.
                #The fix for 4. is to break the loop so it goes to the end.

        if guess == number_to_guess: #1. In all of these if statements it is comparing a str and a int. Runtime error. You can't compare a str and a int using operators.
            print("Congratulations! You've guessed the number!")
            game_over = True
            break

        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts = attempts + 1 #The fix for 2. will just be to make it go up one.

        elif guess < number_to_guess:
            print("Too low! Try again.")  
            attempts = attempts + 1
        
        continue
    print("Game Over. Thanks for playing!")

start_game()