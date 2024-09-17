#Sawyer Wood, Graded Quiz proficiencytest

Correct = 0
Wrong = 0
WhatIsYourAnswer = "What do you think the answer is(Please capitalize the first word)?: "
Question1 = "The first question is, what color are Zebras?"
Question2 = "The second question is, what is the sqrt(4)?"
Question3 = "The third question is, how many colors and in the rainbow?"
Question4 = "The fourth question is, do octopuses have bones?"
Question5 = "How many kilometers up does the atmosphere end?" 


print(Question1)
Personanswer1 = str(input(WhatIsYourAnswer))

if Personanswer1 == str("Black and white" or "White and black"):
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print(Question2)
Personanswer2 = str(input(WhatIsYourAnswer))

if Personanswer2 == str("2" or "Two"):
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print(Question3)
Personanswer2 = str(input(WhatIsYourAnswer))

if Personanswer2 == str("7" or "Seven"):
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print(Question4)
Personanswer2 = str(input(WhatIsYourAnswer))

if Personanswer2 == str("No"):
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print(Question5)
Personanswer2 = str(input(WhatIsYourAnswer))

if Personanswer2 == str("100" or "One hndred"):
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print("That was the last question. You got", Correct, "answers correct and", Wrong, "answers wrong.")