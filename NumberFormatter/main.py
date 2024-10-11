#Sawyer Wood, What are these numbers proficiency test.

while True:
    def format(num):

        text1 = "The number with commas is {:,}"
        text2 = "With decimals(only to the fourth) is {:.4f}"
        text3 = "The number as a percent is {:%}"
        text4 = "The number as a dollar amount is ${:.2f}"

        print(text1.format(num))
        print(text2.format(num))
        print(text3.format(num))
        print(text4.format(num))


    floatorint = input("Is it a float or an int? ")

    if floatorint in ["int", "i", "Int", "I"]:
        num = int(input("What is the int you want to formant? "))
        format(num)

    elif floatorint in ["float", "f", "Float", "F"]:
        num = float(input("What is the float you want to formant? "))
        format(num)

    elif floatorint == "p":
        break