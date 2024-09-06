#This is for fun
#Find out what is wrong with the Outputwanted not like having to options it could be for the "if" statements.
#So I can do math :|
import math

Outputwanted = input("What side of the triandle are you trying to find, Leg or Hypotenuse?: ")

if Outputwanted == str("l"):
  Leg1Length = input("What is the length of leg 1?: ")
  Hypotenuse = input("What is the legnth of the hypotenuse?: ")
  Leg1Length = int(Leg1Length)
  Hypotenuse = int(Hypotenuse)
  Leg2Length = (math.sqrt((Hypotenuse **2) - (Leg1Length **2)))

  if Leg2Length < 0:
      Leg2Length = str(Leg2Length)
      print ("This is not a possible triangle.")
    
  if Leg2Length > 0:
     Leg2Length = str(Leg2Length)
     print ("The length of the leg is", Leg2Length)

if Outputwanted == str("h"):
  Leg1Length = input("What is the length of leg 1?: ")
  Leg2Length = input("What is the length of leg 2?: ")
  Leg1Length = int(Leg1Length)
  Leg2Length = int(Leg2Length)
  Hypotenuse = (math.sqrt((Leg1Length **2) + (Leg2Length **2)))
  Hypotenuse = str(Hypotenuse)
  print ("The length of the hypotenuse is", Hypotenuse)
