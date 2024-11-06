#Sawyer Wood, tic-tac-toe game, proficiency test

import random

Spot1 = ""
Spot2 = ""
Spot3 = ""
Spot4 = ""
Spot5 = ""
Spot6 = ""
Spot7 = ""
Spot8 = ""
Spot9 = ""

botmoves = ["Spot1", "Spot2", "Spot3", "Spot4", "Spot5", "Spot6", "Spot7", "Spot8", "Spot9"]

def check_win(board):
    if board[0 or 1 or 2] == ['X', 'X', 'X']:
        print("Player Won.")
        return True
    
    if board[0 or 1 or 2] == ['O', 'O', 'O']:
        print("Computer Won.")
        return True

for x in range(10):
    board = [
    [Spot1, Spot2, Spot3],
    [Spot4, Spot5, Spot6],
    [Spot7, Spot8, Spot9]
    ]
    #for x in board:
        #for i in x:
            #print(i)
    print(f"{board[0]}\n{board[1]}\n{board[2]}")
    playermove = int(input("What spot do you want to take?(1-9)\t"))

    if playermove == 1 and Spot1 == "":
        Spot1 = "X"
        botmoves.remove("Spot1")

    elif playermove == 2 and Spot2 == "":
        Spot2 = "X"
        botmoves.remove("Spot2")

    elif playermove == 3 and Spot3 == "":
        Spot3 = "X"
        botmoves.remove("Spot3")

    elif playermove == 4 and Spot4 == "":
        Spot4 = "X"
        botmoves.remove("Spot4")

    elif playermove == 5 and Spot5 == "":
        Spot5 = "X"
        botmoves.remove("Spot5")

    elif playermove == 6 and Spot6 == "":
        Spot6 = "X"
        botmoves.remove("Spot6")
    
    elif playermove == 7 and Spot7 == "":
        Spot7 = "X"
        botmoves.remove("Spot7")

    elif playermove == 8 and Spot8 == "":
        Spot8 = "X"
        botmoves.remove("Spot8")

    elif playermove == 9 and Spot9 == "":
        Spot9 = "X"
        botmoves.remove("Spot9")
    else:
        print("This spot is taken.")
    
    if check_win(board) == True:
        break
    
    botmove = random.choice(botmoves)
    if botmove == "Spot1":
        Spot1 = "O"
        botmoves.remove("Spot1")

    elif botmove == "Spot2":
        Spot2 = "O"
        botmoves.remove("Spot2")

    elif botmove == "Spot3":
        Spot3 = "O"
        botmoves.remove("Spot3")

    elif botmove == "Spot4":
        Spot4 = "O"
        botmoves.remove("Spot4")

    elif botmove == "Spot5":
        Spot5 = "O"
        botmoves.remove("Spot5")

    elif botmove == "Spot6":
        Spot6 = "O"
        botmoves.remove("Spot6")

    elif botmove == "Spot7":
        Spot7 = "O"
        botmoves.remove("Spot7")

    elif botmove == "Spot8":
        Spot8 = "O"
        botmoves.remove("Spot8")

    elif botmove == "Spot9":
        Spot9 = "O"
        botmoves.remove("Spot9")
    
    if check_win(board) == True:
        break