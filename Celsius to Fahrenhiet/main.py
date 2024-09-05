#Sawyer Wood, Celsius to Fahrenhiet calculator.

Inputype = input("What type of degrees are you putting into the claclulator? F or C or K: ")

if Inputype == str("C"):

    Celsius = input("What Celsius temperature is it?: ")
    Celsius = int(Celsius)
    Fahrenhiet = (Celsius * (9/5))+32
    Kelvin = (Celsius + 273.15)

    print (Celsius, "degrees Celsius is" ,Fahrenhiet, "degrees Fahrenhiet and" ,Kelvin, "degrees Kelvin.")

if Inputype == str("F"):
    Fahrenhiet = input("What Fahrenhiet temperature is it?: ")
    Fahrenhiet = int(Fahrenhiet)
    Celsius = (Fahrenhiet - 32)*(5/9)
    Kelvin = (Celsius +273.15)

    print (Fahrenhiet, "degrees Fahrenhiet is" ,Celsius, "Degrees Celsius and" ,Kelvin, "degrees Kelvin.")

if Inputype == str("K"):

    Kelvin = input("What Kelvin is it?: ")
    Kelvin = int(Kelvin)
    Celsius = (Kelvin - 273.15)
    Fahrenhiet = (Celsius * 9/5)+32

    print (Kelvin, "degrees Kelvin is" ,Celsius, "degrees Celsius and" ,Fahrenhiet, "degrees Fahrenhiet.")