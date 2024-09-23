#Sawyer Wood, Anagram Creator RAID
import random

name = input("What is your name?: ")
num = len(name)
counter = num
while counter > -1:
    print(name[random.randint(0, num)])
    counter = counter - 1