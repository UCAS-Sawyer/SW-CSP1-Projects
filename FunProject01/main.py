#4fun
#You need to put "pip install mouse" into your terminal.

import keyboard
import random
money = 100
prize1 = 5
prize2 = 15
prize3 = 30
prize4 = 70
prize5 = 145
jackpot = 300
casinogain = 0
spincount = 0
guesscount = 0
print("Starting")
TheWayYouWantToLooseYourMoney = input("What is your desired choice of gambling?(Spin or Guess): ")
TheWayYouWantToLooseYourMoney = TheWayYouWantToLooseYourMoney.lower()

if TheWayYouWantToLooseYourMoney == "guess":
    print("Press G to guess")
    while money > 0:
        if keyboard.read_key() == "p":
         money = 0
         print("You forfeit")

        elif keyboard.read_key() == "c":
            print(guesscount)

        elif keyboard.read_key() == "g":
            guess = int(input("What number do you want to guess.(1-100, if it is over the number you fail): "))
            goal = random.randint(0,100)
            money -= 20
            casinogain += 20

            print(f"You guessed {guess} the number was {goal}.")

            if guess == goal:
                money = money + jackpot
                casinogain = casinogain - jackpot
                guesscount += 1
                print(f"You guess the right number, you got {jackpot}$, you have {money}$ and the casino has gained {casinogain}$")
            
            elif guess == 50 - 3 or 2 or 1:
                money = money + prize5
                casinogain = casinogain - prize5
                print(f"You guess within three of the right number, you got {prize5}$, you have {money}$ and the casino has gained {casinogain}$")

            elif guess > goal:
                print(f"You guessed too high, you have {money}$ and the casino has gained {casinogain}$")
                continue




if TheWayYouWantToLooseYourMoney == "spin":
    print("Press S to spin.")
    while money > 0:

        if keyboard.read_key() == "p":
         money = 0
         print("You forfeit")

        if keyboard.read_key() == "c":
            print(spincount)

        if keyboard.read_key() == "s":
            spincount = spincount + 1
            if spincount <= 50:
                money = money - 20
                casinogain = casinogain + 20
            else:
                money = money -30
                casinogain = casinogain + 30
            num = random.randint(0,100)
            if num <= 50:
                money = money + prize1
                casinogain = casinogain - prize1
                print("You rolled", num, "You won", prize1, "dollars!")
            
            if 75 >= num > 50:
                money = money + prize2
                casinogain = casinogain - prize2
                print("You rolled", num, "You won", prize2, "dollars!")

            if 87 >= num > 75:
                money = money + prize3
                casinogain = casinogain - prize3
                print("You rolled", num, "You won", prize3, "dollars!")

            if 93 >= num > 87:
                money = money + prize4
                casinogain = casinogain - prize4
                print("You rolled", num, "You won", prize4, "dollars!")
        
            if 99 >= num > 93:
                money = money + prize5
                casinogain = casinogain - prize5
                print("You rolled", num, "You won", prize5, "dollars!")
        
            if num == 100:
                money = money + jackpot
                casinogain = casinogain - jackpot
                print("You won", jackpot, "dollars!")
        print("You currently have", money, "dollars and the casino has made",casinogain, "dollars!")