#Sawyer Wood, Anagram Creator RAID
import random
name = input("What is your name?: ")
counter = 0
num = int(input("How many anagrams do you want?: "))

while counter < num:
    counter = counter + 1
    name = list(name)
    random.shuffle(name)
    name = ''.join(name)
    print(name)