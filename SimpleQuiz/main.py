#Sawyer Wood, simple quiz game, proficiency test.

import random

gotright = 0
gotwrong = 0

print("The topic is: Dolphins\n")

Easyquestions = [
    {"Question" : "What is the biggest dolphin?\nA. Bottlenose\nB. Orca\nC. Maui's dolphin\nD. Pilot whale", "Answer" : "b"},
    {"Question" : "Most dolphin species the females are bigger than the males.\nA. True\nB. False", "Answer" : "a"},
    {"Question" : "Dolphins do not have echolocation.\nA. True\nB. False", "Answer" : "b"}
    ]

Hardquestions = [
    {"Question" : "What is the smallest dolphin?\nA. Ganges river dolphin\nB. Pygmy killer whale\nC. Hector's dolphin\nD. Right whale dolphin", "Answer" : "c"},
    {"Question" : "Dolphins primarily eat which type of fish?\nA. Rainbow trout\nB. Shark\nC. Angel fish\nD. Tuna", "Answer" : "d"},
    {"Question" : "Dolphins communicate using a variety of_____\nA. Only clicks and whistles\nB. Only nonverbal communication\nC. Only clicks and whistles with nonverbal\nD. Clicks, whistles, other vocalizations and nonverbal", "Answer" : "d"}
    ]

for x in Hardquestions:
    print(x["Question"])
    playeranswer = input("")
    playeranswer = playeranswer.lower()
    if playeranswer == x["Answer"]:
        print("You got it correct.")
        gotright += 1

    else:
        print("You got it wrong. Here is an easier question")
        gotwrong += 1
        print(Easyquestions[0]["Question"])
        playeranswer = input("")
        playeranswer = playeranswer.lower()
        if playeranswer == Easyquestions[0]["Answer"]:
            print("You got it right.")
            gotright += 1
        else:
            print("You got it wrong.")
            gotwrong += 1
        Easyquestions.pop(0)
else:
    print(f"You got {gotright} answers right and {gotwrong} wrong.")