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

    if board[0] == ['X', 'X', 'X']:
        print("Player Won.")
        return True
    
    elif board[0] == ['O', 'O', 'O']:
        print("Computer Won.")
        return True

    if board[1] == ['X', 'X', 'X']:
        print("Player Won.")
        return True
    
    elif board[1] == ['O', 'O', 'O']:
        print("Computer Won.")
        return True
    
    if board[2] == ['X', 'X', 'X']:
        print("Player Won.")
        return True
    
    elif board[2] == ['O', 'O', 'O']:
        print("Computer Won.")
        return True

    elif Spot1 == 'X' and Spot4 == 'X' and Spot7 == 'X':
        print("Player Won.")
        return True
    
    elif Spot1 == "O" and Spot4 == "O" and Spot7 == 'O':
        print("Computer Won.")
        return True
    
    elif Spot2 == 'X' and Spot5 == 'X' and Spot8 == 'X':
        print("Player Won.")
        return True
    
    elif Spot2 == "O" and Spot5 == "O" and Spot8 == 'O':
        print("Computer Won.")
        return True
    
    elif Spot3 == 'X' and Spot6 == 'X' and Spot9 == 'X':
        print("Player Won.")
        return True
    
    elif Spot3 == "O" and Spot6 == "O" and Spot9 == 'O':
        print("Computer Won.")
        return True
    
    elif Spot1 == 'X' and Spot5 == 'X' and Spot9 == 'X':
        print("Player Won.")
        return True
    
    elif Spot1 == "O" and Spot5 == "O" and Spot9 == 'O':
        print("Computer Won.")
        return True
    
    elif Spot3 == 'X' and Spot5 == 'X' and Spot7 == 'X':
        print("Player Won.")
        return True
    
    elif Spot3 == "O" and Spot5 == "O" and Spot7 == 'O':
        print("Computer Won.")
        return True

    elif Spot1 and Spot2 and Spot3 and Spot4 and Spot5 and Spot6 and Spot7 and Spot8 and Spot9 != "":
        print("Tie")
        return True

while True:
    board = [
    [Spot1, Spot2, Spot3],
    [Spot4, Spot5, Spot6],
    [Spot7, Spot8, Spot9]
    ]
    
    for x in board:
        linetext = ""
        for i in x:
            linetext = linetext + i + " | "
        
        print(linetext)

    if check_win(board) == True:
        break

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
        continue

    board = [
    [Spot1, Spot2, Spot3],
    [Spot4, Spot5, Spot6],
    [Spot7, Spot8, Spot9]
    ]

    for x in board:
        linetext = ""
        for i in x:
            linetext = linetext + i + " | "
        
        print(linetext)

    if check_win(board) == True:
        break
    
    print("Bot Goes")
    
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
        