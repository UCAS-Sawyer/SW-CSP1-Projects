#Sawyer Wood, Fibonacci Sequance RAID.

Origin1 = float(input("What is your first number?: "))
Origin2 = float(input("What is your second number?: "))
HowManyTimes = int(input("How many unmbers do you want?: "))
HowManyTimes = HowManyTimes - 3
Count = 0
print(Origin1)
print(Origin2)

while Count <= HowManyTimes:
    Count = Count + 1
    Current = Origin1 + Origin2
    print(Current)
    Origin1 = Origin2
    Origin2 = Current