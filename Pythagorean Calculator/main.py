#This is for fun

import math

Outputwanted = input("What side of the triandle are you trying to find, Leg or Hypotenuse?: ")

if Outputwanted == str("L" or "Leg"):
  Leg1Length = input("What is the length of leg 1?: ")
  Hypotenuse = input("What is the legnth of the hypotenuse?: ")
  Leg1Length = int(Leg1Length)
  Hypotenuse = int(Hypotenuse)

  if Hypotenuse <= Leg1Length:
    print ("This is not a triangle")
  else:
    Leg2Length = (math.sqrt((Hypotenuse **2) - (Leg1Length **2)))
    Leg2Length = str(Leg2Length)
    print ("The length of the leg is", Leg2Length)


if Outputwanted == str("H" or "Hypotenuse"):
  Leg1Length = input("What is the length of leg 1?: ")
  Leg2Length = input("What is the length of leg 2?: ")
  Leg1Length = int(Leg1Length)
  Leg2Length = int(Leg2Length)
  Hypotenuse = (math.sqrt((Leg1Length **2) + (Leg2Length **2)))
  Hypotenuse = str(Hypotenuse)
  print ("The length of the hypotenuse is", Hypotenuse)