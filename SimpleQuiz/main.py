#Sawyer Wood, simple quiz game, proficiency test.

import random

gotright = 0
gotwrong = 0

print("The topic is: Dolphins\nPlease just use lowercase.")
Equestion1 = "What is the biggest dolphin?\nA. Bottlenose\nB. Orca\nC. Maui's dolphin\nD. Pilot whale"
Equestion2 = "Most dolphin species the females are bigger than the males.\nA. True\nB. False"
Equestion3 = "Dolphins do not have echolocation.\nA. True\nB. False"

Eanswer1 = "b"
Eanswer2 = "a"
Eanswer3 = "b"

Easyanswer = [Eanswer1, Eanswer2, Eanswer3]
Easyquestions = [Equestion1, Equestion2, Equestion3]

Hquestion1 = "What is the smallest dolphin?\nA. Ganges river dolphin\nB. Pygmy killer whale\nC. Hector's dolphin\nD. Right whale dolphin "
Hquestion2 = "Dolphins communicate using a variety of_____\nA. Only clicks and whistles\n B. Only nonverbal communication\nC. Only clicks and whistles with nonverbal\nD. Clicks, whistles, other vocalizations and nonverbal"

Hanswer1 = "c"
Hanswer2 = "d"

Hardanswer =[Hanswer1, Hanswer2]
Hardquestions = [Hquestion1, Hquestion2]

Elen = len(Easyquestions)
indexnum = random.randint(0,Elen)
print(Easyquestions[indexnum])
playeranswer = input("")
if playeranswer == Easyanswer[indexnum]:
    print("You got it correct.")
    gotright += 1
    Easyquestions.pop(indexnum)
    Easyanswer.pop(indexnum)
    Hlen = len(Hardquestions)
    indexnum = random.randint(0,Hlen)
    print(Hardquestions[indexnum])
    playeranswer = input("")
    if playeranswer == Hardanswer[indexnum]
        print("You got it correct.")
        gotright += 1
        Hardquestions.pop(indexnum)
        Hardanswer.pop(indexnum)
    else:
        print("You got it wrong.")
        gotwrong += 1
        Elen = len(Easyquestions)
        indexnum = random.randint(0,Elen)
        print(Easyquestions[indexnum])
        playeranswer = input("")
        if playeranswer == Easyanswer[indexnum]:
            print("You got it correct.")
        else:
            print("You got it wrong.")
            gotwrong += 1
else:
    print("You got it wrong.")
    gotwrong += 1
    