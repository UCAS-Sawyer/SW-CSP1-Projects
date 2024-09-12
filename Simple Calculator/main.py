#Sawyer Wood, Simple Calculator proficiencytest.

MathTypeWanted = input("What do you want to do(Multiplication, Addition ect.. or you can just use the symbols)?: ")

#Addition
if MathTypeWanted == str("+" or "Addition"):
    FirstNum = float(input("What is your first number?: "))
    SecondNum = float(input("What is your second number?: "))
    Answer = FirstNum + SecondNum
    AnswerRounded = round(Answer, 4)
    if AnswerRounded != Answer:
        AnswerRounded = str(AnswerRounded)
        print("The answer is", AnswerRounded, "(It is rounded)")
    else:
        Answer = str(Answer)
        print("The answer is", Answer)

#Subtraction
if MathTypeWanted == str("-" or "Subtraction"):
    FirstNum = float(input("What is your first number?: "))
    SecondNum = float(input("What is your second number?: "))
    Answer = FirstNum - SecondNum
    AnswerRounded = round(Answer, 4)
    if AnswerRounded != Answer:
        AnswerRounded = str(AnswerRounded)
        print("The answer is", AnswerRounded, "(It is rounded)")
    else:
        Answer = str(Answer)
        print("The answer is", Answer)

#Multiplication
if MathTypeWanted == str("*" or "Multiplication"):
    FirstNum = float(input("What is your first number?: "))
    SecondNum = float(input("What is your second number?: "))
    Answer = FirstNum * SecondNum
    AnswerRounded = round(Answer, 4)
    if AnswerRounded != Answer:
        AnswerRounded = str(AnswerRounded)
        print("The answer is", AnswerRounded, "(It is rounded)")
    else:
        Answer = str(Answer)
        print("The answer is", Answer)

#Division
if MathTypeWanted == str("/" or "Division"):
    FirstNum = float(input("What is your first number?: "))
    SecondNum = float(input("What is your second number?: "))
    Answer = FirstNum / SecondNum
    AnswerRounded = round(Answer, 5)
    if AnswerRounded != Answer:
        AnswerRounded = str(AnswerRounded)
        print("The answer is", AnswerRounded, "(It is rounded)")
    else:
        Answer = str(Answer)
        print("The answer is", Answer)

#Exponents
if MathTypeWanted == str("**" or "Exponential"):
    FirstNum = float(input("What is your first number?: "))
    SecondNum = float(input("What is your second number?: "))
    Answer = FirstNum ** SecondNum
    AnswerRounded = round(Answer, 4)
    if AnswerRounded != Answer:
        AnswerRounded = str(AnswerRounded)
        print("The answer is", AnswerRounded, "(It is rounded)")
    else:
        Answer = str(Answer)
        print("The answer is", Answer)

#Modulus
if MathTypeWanted == str("%" or "Modulus"):
    FirstNum = float(input("What is your first number?: "))
    SecondNum = float(input("What is your second number?: "))
    Answer = FirstNum % SecondNum
    Answer = str(Answer)
    print("There is", Answer, "Left after dividing")