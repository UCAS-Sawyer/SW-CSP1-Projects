#Sawyer Wood, Graded Quiz proficiencytest

Correct = 0
Wrong = 0
WhatIsYourAnswer = "What do you think the answer is(Please capitalize the first word)?: "
Question1 = "The first question is, what color are Zebras?"
Answer1 = str("Black and white" or "White and black")
Question2 = "The second question is, what is the sqrt(4)?"
Answer2 = str("2" or "Two")
Question3 = "The third question is, how many colors and in the rainbow?"
Answer3 = str("7" or "Seven")
Question4 = "The fourth question is, do octopuses have bones?"
Answer4 = str("No")
Question5 = "How many kilometers up does the atmosphere end?" 
Answer5 = str("100" or "One hndred")

print(Question1)
Personanswer1 = str(input(WhatIsYourAnswer))

if Personanswer1 == Answer1:
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print(Question2)
Personanswer2 = str(input(WhatIsYourAnswer))

if Personanswer2 == Answer2:
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print(Question3)
Personanswer3 = str(input(WhatIsYourAnswer))

if Personanswer3 == Answer3:
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print(Question4)
Personanswer4 = str(input(WhatIsYourAnswer))

if Personanswer4 == Answer4:
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print(Question5)
Personanswer5 = str(input(WhatIsYourAnswer))

if Personanswer5 == Answer5:
    Correct = Correct + 1
else:
    Wrong = Wrong + 1

print("That was the last question. You got", Correct, "answers correct and", Wrong, "answers wrong.")